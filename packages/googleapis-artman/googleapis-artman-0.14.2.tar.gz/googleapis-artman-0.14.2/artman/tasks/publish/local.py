# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, unicode_literals
import functools
import os
import uuid

import github3

import six

from artman.tasks import task_base
from artman.utils.logger import logger


class LocalStagingTask(task_base.TaskBase):
    """Create a new branch on GitHub with the appropriate GAPIC.

    This task requires WRITE access to the applicable repository.
    """
    def execute(self, git_repo, output_dir,
        gapic_code_dir=None, grpc_code_dir=None, proto_code_dir=None,
        local_repo_dir=None):
        """Copy the code to the correct local staging location.

        Args:
            gapic_code_dir (str): The location of the GAPIC code.
            git_repo (dict): Information about the git repository.
            output_dir (str): The original base output dir. This directory
                is removed after proper local code staging unless removing
                it would remove the final destination directories.
            grpc_code_dir (str): The location of the GRPC code, if any.
        """
        # Determine the actual repository name.
        # We can use this to derive the probable OS system path.
        repo_name = git_repo['location'].rstrip('/').split('/')[-1]
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]

        # Artman will find the local repo dir via the following steps:
        # 1. Check whether an explicit `--local_repo_dir` flag is passed. Is so,
        #    use that value.
        # 2. Clones the repo to output_dir, and use the cloned repo dir.
        repo_name_underscore = repo_name.replace('-', '_')
        if local_repo_dir:
            api_repo = local_repo_dir
        else:
            api_repo = os.path.join(output_dir, repo_name)
            if os.path.exists(api_repo):
                logger.fatal(
                    'Local repo folder `%s` exists. Please manually remove the '
                    'folder, or point to another folder through artman user '
                    'config or `artman --output-dir` flag.' % api_repo)
            repo = git_repo['location']
            # This only works for public repo for now.
            if repo.startswith('git@github.com:'):
                repo = 'https://github.com/%s' % repo[15:]
            logger.info('Checking out fresh clone of %s.' % repo)
            self.exec_command(['git', 'clone', repo, api_repo])

        # Track our code directories, and use absolute paths, since we will
        # be moving around.
        code_dirs = {}
        if gapic_code_dir:
            code_dirs['gapic'] = os.path.abspath(gapic_code_dir)
        if grpc_code_dir:
            code_dirs['grpc'] = os.path.abspath(grpc_code_dir)
        if proto_code_dir:
            code_dirs['proto'] = os.path.abspath(proto_code_dir)

        if not code_dirs:
            raise RuntimeError('No code path is defined.')

        # Keep track of all destinations so we are not too eager on wiping
        # out code from the original output area.
        #
        # This also allows useful output to the user in the success message.
        dests = []

        # Sanity check: The git repository must explicitly define the paths
        # where the generated code goes. If that is missing, fail now.
        if not git_repo.get('paths'):
            raise RuntimeError('This git repository entry in the artman YAML '
                               'does not define module paths.')

        # Determine where the code belongs and stage it there.
        for path in git_repo['paths']:
            # Piece together where we are copying code from and to.
            if isinstance(path, (six.text_type, six.binary_type)):
                path = {'dest': path}
            artifact = path.get('artifact', 'gapic')

            if artifact in code_dirs:
                # Convert everything to an absolute path.
                src = os.path.abspath(os.path.join(code_dirs[artifact], path.get('src', '.')))
                dest = os.path.abspath(os.path.join(api_repo, path.get('dest', '.')))

                # All src path does not necessarily exist. For example, gapic src directory will
                # not be created for ProtoClientPipeline
                if os.path.isdir(src):
                    # Keep track of all code destinations, for output later.
                    dests.append(dest)

                    # Actually copy the code.
                    self.exec_command(['rm', '-rf', dest])
                    self.exec_command(['cp', '-rf', src, dest])

        # Remove the original paths.
        if gapic_code_dir and os.path.isdir(gapic_code_dir):
            self.exec_command(['rm', '-rf', gapic_code_dir])
        if grpc_code_dir and os.path.isdir(grpc_code_dir):
            self.exec_command(['rm', '-rf', grpc_code_dir])
        if not os.getenv('RUNNING_IN_ARTMAN_DOCKER'):
            if all([output_dir not in d for d in dests]) and os.path.isdir(output_dir):
                self.exec_command(['rm', '-rf', output_dir])

        # Log a useful success message.
        userhome = os.path.expanduser('~')
        for d in dests:
            location = d.replace(userhome, '~')
            logger.success('Code generated: {0}'.format(location))


TASKS = (
    LocalStagingTask,
)
