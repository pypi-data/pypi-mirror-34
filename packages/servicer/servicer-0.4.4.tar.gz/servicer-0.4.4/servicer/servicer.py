import os
import sys
import importlib
import json
import argparse
import yaml
import re

from .generate_ci_config import generate_ci_config
from .topological_order import toposort2
from .run import run
from .git import Git

class Servicer():
    def __init__(self):
        self.run = run
        self.git = Git(hide_output=('DEBUG' not in os.environ))

        args = self.load_arguments()

        args_dict = vars(args)
        self.load_environment(args_dict)
        self.config = self.load_config(args_dict)

        self.normalize_ci_environment()
        self.services = self.load_service_modules()
        self.service_order = self.order_services(self.services)

        if self.config['args']['generate_ci']:
            generate_ci_config(config=config, path='.')
            sys.exit(0)

        self.config['args']['step'] = self.config['args']['step'].split(',')

    def load_arguments(self):
        parser = argparse.ArgumentParser(description='Process deployment options.')
        parser.add_argument('--generate_ci', action='store_true', help='generate a ci config file, do not run any deploy options')
        parser.add_argument('--service', help='deploy only the provided service')
        parser.add_argument('--services_file', default='services.yaml', help='custom path to your services config file (default is services.yaml)')
        parser.add_argument('--servicer_config_path', default=f'{os.getcwd()}/.servicer', help='path to your servicer directory (default is ./servicer)')
        parser.add_argument('--step', default='deploy', help='perform the comma-separated build steps, defaults to deploy only')
        return parser.parse_args()

    def load_environment(self, args):
        env_file = '%s/.env.yaml' % args['servicer_config_path']

        print('checking for (.env.yaml) at (%s)' % env_file)
        if os.path.exists(env_file):

            print('(.env.yaml) found, including these arguments:')

            yaml_dict = yaml.load(open(env_file))
            for key, value in yaml_dict.items():
                os.environ[key] = value
                print(key)
            print()

    def load_config(self, args):
        services_config_file = '%s/%s' % (args['servicer_config_path'], args['services_file'])
        print(f'loading services config from ({services_config_file})')
        services_config = {}
        self.load_extended_config(config_path=services_config_file, config=services_config)

        services_config['config_path'] = args['servicer_config_path']
        services_config['module_path'] = globals()['__file__'].replace('/servicer.py', '')
        services_config['args'] = args

        if 'git' not in services_config:
            services_config['git'] = {}
        if 'enabled' not in services_config['git']:
            services_config['git']['enabled'] = True
        if 'default-branch' not in services_config['git']:
            services_config['git']['default-branch'] = 'master'
        if 'ignore-unchanged' not in services_config['git']:
            services_config['git']['ignore-unchanged'] = True

        if 'environment' in services_config:
            if 'variables' in services_config['environment']:
                for key, value in services_config['environment']['variables'].items():
                    os.environ[key] = value

        print('Services Config:')
        print(json.dumps(services_config, indent=4, sort_keys=True))

        return services_config

    # recursively load configs, overwriting base config values
    def load_extended_config(self, config_path=None, config=None):
        merge_config = yaml.load(open(config_path))

        if 'extends' in merge_config:
            config_path_pieces = config_path.split('/')
            inherit_path = '%s/%s' % ('/'.join(config_path_pieces[:-1]), merge_config['extends'])
            self.load_extended_config(config_path=inherit_path, config=config)
            print('Inheriting: %s' % inherit_path)

        self.merge_config(config, merge_config)

    def merge_config(self, merge_to, merge_from):
        for key, value in merge_from.items():
            if isinstance(value, dict):
                # get node or create one
                node = merge_to.setdefault(key, {})
                self.merge_config(node, value)
            else:
                merge_to[key] = value

        return merge_to

    def normalize_ci_environment(self):
        self.print_title('normalizing CI environment')

        self.config['ci']['adapters'] = {}
        for p in self.config['ci']['providers']:
            print('CI Adapter: %s' % p)
            ci_adapter_modules = [
                {
                    'name': 'ci_adapters.%s' % p,
                    'package': 'ci_adapters',
                    'file_path': '%s/ci_adapters/%s.py' % (self.config['config_path'], p),
                },
                {
                    'name': 'servicer.builtin.ci_adapters.%s' % p,
                    'package': 'servicer.builtin.ci_adapters',
                    'file_path': '%s/builtin/ci_adapters/%s.py' % (self.config['module_path'], p),
                },
            ]
            module = self.load_module_from_paths(ci_adapter_modules)
            self.config['ci']['adapters'][p] = module.CIAdapter()

        for ci_adapter in self.config['ci']['adapters'].values():
            ci_adapter.convert_environment_variables()

        print()
        self.service_environment = os.getenv('SERVICE_ENVIRONMENT') or self.get_service_environment(os.environ['BRANCH'])

        print('service environment: %s' % self.service_environment)
        if self.service_environment:
            os.environ['SERVICE_ENVIRONMENT'] = self.service_environment

    def load_service_modules(self):
        self.print_title('loading service modules')

        services = {}
        if self.config['args']['service']:
            service_names = self.config['args']['service'].split(',')
            for name, service in self.config['services'].items():
                if name in service_names:
                    services[name] = service
        else:
            services = self.config['services']

        self.ignore_unchanged_services(services)

        for service_name, service in services.items():
            if 'config' not in service:
                service['config'] = {}

            self.initialize_provider(service['provider'], service)

            service['name'] = service_name
            service_modules = [
                {
                    'name': 'service_adapters.%s.%s' % (service['provider'], service['service_type']),
                    'package': 'service_adapters',
                    'file_path': '%s/service_adapters/%s/%s.py' % (self.config['config_path'], service['provider'], service['service_type']),
                },
                {
                    'file_path': '%s/service_adapters/%s/%s.sh' % (self.config['config_path'], service['provider'], service['service_type']),
                },
                {
                    'name': 'servicer.builtin.service_adapters.%s.%s' % (service['provider'], service['service_type']),
                    'package': 'servicer.builtin.service_adapters',
                    'file_path': '%s/builtin/service_adapters/%s/%s.py' % (self.config['module_path'], service['provider'], service['service_type']),
                },
                {
                    'file_path': '%s/builtin/service_adapters/%s/%s.sh' % (self.config['module_path'], service['provider'], service['service_type']),
                },
            ]
            module = self.load_module_from_paths(service_modules)
            if isinstance(module, str):
                service['shell_script'] = service['module']
            else:
                service['module'] = module

        return services

    def ignore_unchanged_services(self, services):
        if not (self.config['git']['enabled'] and self.config['git']['ignore-unchanged']):
            return

        git_ref = self.config['git']['default-branch']

        if 'BRANCH' in os.environ:
            sanitized_tag = 'servicer-%s' % self.git.sanitize_tag(os.environ['BRANCH'])
            tags = [t for t in self.git.list_tags() if t.startswith(sanitized_tag)]

            if os.getenv('DEBUG'):
                print('branch tag: %s' % sanitized_tag)
                print('matching tags:')
                print('\n'.join(tags))

            if len(tags) > 0:
                git_ref = tags[-1]

        print('\nGit Ref: %s' % git_ref)
        diff_files = self.git.files_changed_ahead_of_ref(git_ref)
        print('\nChanged Files:')
        print('\n'.join(diff_files))

        # TODO: think through what top level 'watch_paths' means
        if 'ignore_paths' in self.config['git']:
            regexes = [self.sanitize_regex(matcher) for matcher in self.config['git']['ignore_paths']]
            matched_files, diff_files = self.match_regexes(diff_files, regexes)

        ignored_services = []
        for service_name, service in services.items():
            service_changed_files = diff_files

            if 'git' in service:
                if 'watch_paths' in service['git']:
                    watch_regexes = [self.sanitize_regex(matcher) for matcher in service['git']['watch_paths']]

                    if os.getenv('DEBUG'):
                        print('\nService: %s' % service_name)
                        print('Matchers:')

                    service_changed_files, _ = self.match_regexes(diff_files, watch_regexes)

                if 'ignore_paths' in service['git']:
                    ignore_regexes = [self.sanitize_regex(matcher) for matcher in service['git']['ignore_paths']]
                    _, service_changed_files = self.match_regexes(service_changed_files, ignore_regexes)

                if len(service_changed_files) > 0:
                    if os.getenv('DEBUG'):
                        print('\nChanged Files:')
                        print('\n'.join(service_changed_files))
                else:
                    ignored_services.append(service_name)

        print('\nIgnored Services:')
        for sn in ignored_services:
            print(sn)
            services.pop(sn)

        print('\nChanged Services:')
        print('\n'.join(services.keys()))

    def sanitize_regex(self, matcher):
        if matcher.startswith('/') and matcher.endswith('/'):
            return matcher[1:-1]

        return matcher.replace('*', '.*')

    # takes a list of strings, and returns a tuple of strings that match and do not match
    def match_regexes(self, strings, regexes):
        if not isinstance(regexes, list):
            regexes = [regexes]

        matches = []
        unmatches = []
        for s in strings:
            for regex in regexes:
                result = re.match(regex, s)

                if os.getenv('DEBUG'):
                    print('%s ~= %s -> %s' % (regex, s, result))

                if result:
                    matches.append(s)
                else:
                    unmatches.append(s)

        return matches, unmatches

    def initialize_provider(self, provider_name, service):
        provider = self.config['providers'].get(provider_name)
        if provider and self.service_environment and not provider.get('initialized'):
            self.print_title('intializing provider: %s' % provider_name)

            # TODO: account for this extra setup in the build image
            if provider_name == 'gcloud' and os.getenv('CI'):
                self.run('apt-get update', shell=True)
                self.run('apt-get install apt-transport-https -y', shell=True)
                self.run('%s/install-google-cloud-sdk.sh' % self.config['module_path'])

            if 'libraries' in provider:
                self.run('%s install %s' % (os.getenv('PIP_EXE', 'pip'), ' '.join(provider['libraries'])), shell=True)
            if 'auth_script' in provider:
                self.print_title('%s authentication' % provider_name)
                auth_script_paths = [
                    { 'file_path': '%s/auth/%s.sh' % (self.config['config_path'], provider_name) },
                    { 'file_path': '%s/builtin/auth/%s.sh' % (self.config['module_path'], provider_name) },
                ]
                auth_script_path = self.load_module_from_paths(auth_script_paths)
                provider['auth_script_path'] = auth_script_path
                self.run(auth_script_path, shell=True)

            provider['initialized'] = True

        if service:
            service['config']['initialized_provider'] = provider

    def load_module_from_paths(self, modules):
        for mp in modules:
            if os.getenv('DEBUG'):
                print('searching for module at: %s' % mp['file_path'])
            if os.path.exists(mp['file_path']):
                if 'name' in mp:
                    if os.getenv('DEBUG'):
                        print('importing: %s:%s' % (mp['name'], mp['package']))

                    module = importlib.import_module(mp['name'])
                    return module
                else:
                    print('found matching executable: %s' % mp['file_path'])
                    return mp['file_path']

        print('no module found!')
        sys.exit(1)

    def order_services(self, services):
        service_names = services.keys()
        dependencies = {}
        for service_name, service in services.items():
            if 'depends_on' in service:
                dependencies[service_name] = set(service['depends_on'])
            else:
                dependencies[service_name] = set()

        ordered_services = toposort2(dependencies)
        return [item for sublist in ordered_services for item in sublist]

    def run_steps(self):
        for step in self.config['args']['step']:
            self.print_title('%s step' % step)

            if step == 'deploy':
                if self.service_environment:
                    self.up()
                else:
                    print('skipping, no valid deploy environment was matched')
            else:
                for service_name in self.service_order:
                    service = self.services[service_name]

                    if 'steps' in service and step in service['steps']:
                        commands = service['steps'][step].get('commands')
                        if commands:
                            for c in commands:
                                self.run(c, shell=True)

                        if 'module' in service and 'config' in service['steps'][step]:
                            config = service['steps'][step].get('config')
                            print('Step Config (%s): ' % step)
                            print(json.dumps(config, indent=4, sort_keys=True))
                            adapter = service['module'].Service(config)
                            adapter.up()

    def get_service_environment(self, branch):
        print('branch: %s' % branch)
        service_environment = None

        if branch == 'master':
            service_environment = 'production'
        elif branch == 'develop':
            service_environment = 'develop'
        elif branch.startswith('env-'):
            service_environment = branch

        if service_environment:
            for ch in ['\\', '/', '_']:
                if ch in service_environment:
                    service_environment = service_environment.replace(ch, '-')
            return service_environment

    def up(self):
        for service_name in self.service_order:
            print(service_name)

        for service_name in self.service_order:
            self.up_service(self.services[service_name])

        self.print_title('deploy complete')

    def up_service(self, service):
        self.print_title('deploy %s' % service['name'])

        service['results'] = {}

        if 'module' in service:
            adapter = service['module'].Service(service['config'])
            results = adapter.up()
            if results:
                self.store_results(service, results)
        elif 'shell_script' in service:
            self.run('%s up' % service['shell_script'], shell=True)

            # clunky way to retrieve results from shell scripts
            script_results_path = 'shell-script-results.yaml'
            if os.path.exists(script_results_path):
                print('loading script results from (%s)' % script_results_path)
                results = yaml.load(open(script_results_path))
                self.store_results(service, results)
                os.remove(script_results_path)

    def store_results(self, service, results):
        for key, value in results.items():
            if type(value) == str:
                os.environ[key.upper()] = value
        service['results']['up'] = results

    def print_title(self, message='', border='----'):
        inner_text = ' %s ' % message
        border_text = border

        while len(border_text) < len(inner_text):
            border_text = '%s %s' % (border_text, border)

        print()
        print(border_text)
        print(inner_text)
        print(border_text)
        print()

def main():
    Servicer().run_steps()

if __name__ == '__main__':
    main()
