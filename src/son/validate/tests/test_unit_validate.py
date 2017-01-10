#  Copyright (c) 2015 SONATA-NFV, UBIWHERE
# ALL RIGHTS RESERVED.
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
#
# Neither the name of the SONATA-NFV, UBIWHERE
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the SONATA project,
# funded by the European Commission under Grant number 671517 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.sonata-nfv.eu).

import unittest
import os
import son.validate.validate as val
from son.validate.validate import Validator
from son.workspace.workspace import Workspace, Project

SAMPLES_DIR = os.path.join('src', 'son', 'validate', 'tests', 'samples')


class UnitValidateTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(UnitValidateTests, self).__init__(*args, **kwargs)

        # tap log functions to count for errors and warnings
        self._workspace = Workspace('.')
        val.log.error = CountCalls(val.log.error)
        val.log.warning = CountCalls(val.log.warning)

    def test_validate_project_valid(self):
        """
        Tests the validation of a valid SONATA project.
        """
        prj_path = os.path.join(SAMPLES_DIR, 'sample_project_valid')
        project = Project(self._workspace, prj_path)
        validator = Validator(workspace=self._workspace, log_level='debug')
        validator.validate_project(project)

        self.assertEqual(val.log.error.counter, 0)
        self.assertEqual(val.log.warning.counter, 0)

    def test_validate_project_invalid(self):
        """
        Tests the validation of an invalid SONATA project.
        """
        prj_path = os.path.join(SAMPLES_DIR, 'sample_project_invalid')
        project = Project(self._workspace, prj_path)
        validator = Validator(workspace=self._workspace, log_level='debug')
        validator.validate_project(project)

        self.assertGreater(val.log.error.counter, 0)

    def test_validate_project_warning(self):
        """
        Tests the validation of a SONATA project with warnings.
        """
        prj_path = os.path.join(SAMPLES_DIR, 'sample_project_warning')
        project = Project(self._workspace, prj_path)
        validator = Validator(workspace=self._workspace, log_level='debug')
        validator.validate_project(project)

        self.assertEqual(val.log.error.counter, 0)
        self.assertGreater(val.log.warning.counter, 0)




class CountCalls(object):
    """Decorator to determine number of calls for a method"""

    def __init__(self, method):
        self.method = method
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.method(*args, **kwargs)
