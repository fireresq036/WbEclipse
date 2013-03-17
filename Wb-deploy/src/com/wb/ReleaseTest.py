"""
Created on Feb 13, 2013

@author: mrrussell
"""
import unittest
import tempfile
import os
import shutil
from com.wb.Release import Release
from com.wb.FileSystem import FileSystem


class Test(unittest.TestCase):


  def setUp(self):
    self.base = 'base'
    self.tool = 'D2WBtest'
    self.stage = Release.STAGE_CONTINUOUS
    self.file_system = FileSystem(testing=True)
    self._createDirectories()
    self.release = Release(self.base_dir, self.tool, self.stage,
                           file_system=self.file_system)

  def _createDirectories(self):
    tmp_dir = self.file_system.mkdtemp('Rel', 'Test')
    tmp_base = self.file_system.join(tmp_dir, self.base)
    tmp_tool = self.file_system.join(tmp_base, self.tool)
    tmp_stage = self.file_system.join(tmp_tool, self.stage)
    self.version_name = 'v1.2.3.23423'
    self.actual_path = self.file_system.join(tmp_stage, self.version_name)
    self.latest_path = self.file_system.join(tmp_stage, 'latest')
    self.update_path = self.file_system.join(self.actual_path, 'update')
    self.file_system.makedirs(self.update_path)
    self.file_system.symlink(self.actual_path, self.latest_path)
    
    self.zip_count = 0;
    for i in range(1,4):
      zip_file_name = self.file_system.join(self.update_path, 
                                            'zip{0}.zip'.format(i))
      self.file_system.create_file(zip_file_name)
      self.zip_count += 1
    self.temp_dir = tmp_dir
    self.base_dir = tmp_base
    return

  def tearDown(self):
    self.file_system._dump()
    self.file_system.rmtree(self.temp_dir)
    self.file_system._dump()
    self.release = None


  def testZips(self):
    zips = self.release.zips()
    found = []
    for count in range(0,4):
      found.append(False)

    self.assertEqual(self.zip_count, len(zips))
    for zip_file in zips:
      index = zip_file.rfind(self.file_system.sep())
      name = zip_file[index:]
      index = name.rfind('.')
      zip_number = int(name[index - 1])
      found[zip_number] = True
    all_found = True
    for val in found:
      if not val:
        all_found = False
    self.assertTrue('not all zips found', all_found)


  def testLatest(self):
    latest = self.release.latest();
    self.assertIsNotNone(latest)
    self.assertTrue(len(latest) > 0)
    self.assertTrue(self.version_name, latest)


  def testVersions(self):
    versions = self.release.versions();
    self.assertIsNotNone(versions)
    self.assertEqual(1, len(versions))
    self.assertIn(self.version_name, versions)
if __name__ == '__main__':
  #import sys;sys.argv = ['', 'Test.testZips']
  unittest.main()