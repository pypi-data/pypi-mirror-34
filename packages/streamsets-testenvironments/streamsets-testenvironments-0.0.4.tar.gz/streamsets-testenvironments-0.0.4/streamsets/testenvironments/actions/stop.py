# Copyright 2017 StreamSets Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import subprocess

from ..models import Command

logger = logging.getLogger(__name__)


def main(environment_configs, environment_name, config_environment, args, defaults):
    args_name_value_pair = {arg_name.replace('_', '-'): arg_parameter for arg_name, arg_parameter in args.items()}
    config_defaults = {arg_name: arg_parameter.format(**args_name_value_pair)
                       for arg_name, arg_parameter in defaults.items()}

    # args substitution prevails over config_defaults
    stop_commands = ([Command(command.format(**{**config_defaults, **args_name_value_pair}))
                      for command in environment_configs.get('environment_stop')]
                     if 'environment_stop' in environment_configs else [])
    commands = [Command(command.format(**{**config_defaults, **args_name_value_pair}))
                for command in config_environment.get('stop', [])]

    if commands:
        logger.info('Stopping test environment %s ...', environment_name)
        try:
            for command in commands:
                command.execute(dry_run=args['dry_run'])
        finally:
            # execute `environment_stop` command anyway to do any post cleanup - useful for already stopped environments
            for command in stop_commands:
                command.execute(dry_run=args['dry_run'])
    else:
        logger.warning('No test environment stop info found for environment %s', environment_name)
