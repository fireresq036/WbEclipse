"""
Created on Feb 13, 2013

@author: mrrussell
"""
import unittest
import tempfile
import os
import shutil
from com.wb.Release import Release


class Test(unittest.TestCase):


  def setUp(self):
    release = Release
    self.base = 'base'
    self.tool = 'D2WBtest'
    self.stage = release.STAGE_CONTINUOUS
    self.temp_dir = self._createDirectories()
    

  def _createDirectories(self):
    tmp_dir = tempfile.mkdtemp('Rel', 'Test')
    tmp_base = os.path.join(tmp_dir, self.base)
    tmp_tool = os.path.join(tmp_base, self.tool)
    tmp_stage = os.path.join(tmp_tool, self.stage)
    self.actual_path = os.path.join(tmp_stage, 'v1.2.3.23423')
    self.latest_path = os.path.join(tmp_stage, 'latest')
    self.update_path = os.path.join(self.actual_path, 'update')
    os.makedirs(self.update_path)
    os.symlink(self.actual_path, self.latest_path)
    
    for i in range(1,4):
      f = open(os.path.join(self.update_path, 'zip%s.zip' % i), 'w+')
      f.close()

    return tmp_dir

  def tearDown(self):
    shutil.rmtree(self.temp_dir)


  def testZips(self):
    pass


if __name__ == '__main__':
  #import sys;sys.argv = ['', 'Test.testZips']
  unittest.main()