# Copyright 2010 Google Inc. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
import shutil
import tempfile

from absl.testing import absltest
from googleapis.codegen.filesys import files


class FilesTest(absltest.TestCase):

  def setUp(self):
    self.tempdir = tempfile.mkdtemp()
    for name in 'abc':
      with open(os.path.join(self.tempdir, name), 'w') as f:
        f.write(name)

  def tearDown(self):
    shutil.rmtree(self.tempdir)

  def testGetFileContentsLocal(self):
    filename = os.path.join(self.tempdir, 'a')
    contents = files.GetFileContents(filename)
    self.assertEqual(b'a', contents)

  def testIterFilesLocal(self):
    listing = sorted(files.IterFiles(self.tempdir))
    expected = [os.path.join(self.tempdir, x) for x in 'abc']
    self.assertEqual(expected, listing)

  def testIsFileLocal(self):
    self.assertTrue(files.IsFile(os.path.join(self.tempdir, 'a')))
    self.assertFalse(files.IsFile(self.tempdir))

if __name__ == '__main__':
  absltest.main()
