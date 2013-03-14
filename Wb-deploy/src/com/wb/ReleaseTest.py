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
    self._createDirectories()
    self.release = Release(self.base_dir, self.tool, self.stage,
                           file_system=FileSystem(testing=True))
    

  def _createDirectories(self):
    tmp_dir = tempfile.mkdtemp('Rel', 'Test')
    tmp_base = os.path.join(tmp_dir, self.base)
    tmp_tool = os.path.join(tmp_base, self.tool)
    tmp_stage = os.path.join(tmp_tool, self.stage)
    self.version_name = 'v1.2.3.23423'
    self.actual_path = os.path.join(tmp_stage, self.version_name)
    self.latest_path = os.path.join(tmp_stage, 'latest')
    self.update_path = os.path.join(self.actual_path, 'update')
    os.makedirs(self.update_path)
    os.symlink(self.actual_path, self.latest_path)
    
    self.zip_count = 0;
    for i in range(1,4):
      f = open(os.path.join(self.update_path, 'zip%s.zip' % i), 'w+')
      f.close()
      self.zip_count += 1
    self.temp_dir = tmp_dir
    self.base_dir = tmp_base
    return

  def tearDown(self):
    shutil.rmtree(self.temp_dir)
    self.release = None


  def testZips(self):
    zips = self.release.zips()
    self.assertEqual(self.zip_count, len(zips))
    self.assertTrue('zip1.zip' in zips)
    self.assertTrue('zip3.zip' in zips)
    self.assertFalse('zip4.zip' in zips)
    self.assertFalse('zip0.zip' in zips)


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