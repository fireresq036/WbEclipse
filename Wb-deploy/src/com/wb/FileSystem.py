'''
Created on Mar 13, 2013

@author: mrrussell
'''

from com.wb.TestFileSystem import TestFileSystem
from com.wb.RealFileSystem import RealFileSystem
import os

class FileSystem(object):
  '''Handle all interactions with the file system'''

  def __init__(self, testing=False):
    '''
    initialize this class and use a virtual file system if testing is true
    '''
    if testing:
      self.file_system = TestFileSystem()
    else:
      self.file_system = RealFileSystem()

  def sep(self):
    return self.file_system.sep()
  
  def join(self, *args):
    full_path = ''
    for arg in args:
      full_path = os.path.join(full_path, arg)
    return full_path
  
  def readlink(self, path):
    return self.file_system.readlink(path)
  
  def islink(self, path):
    return self.file_system.islink(path)
  
  def listdir(self, dir_path):
    return self.file_system.listdir(dir_path)

  def mkdtemp(self, prefix='tmp', suffix='', directory=None):
    return self.file_system.mkdtemp(prefix, suffix, directory)

  def _dump(self):
    self.file_system._dumpFileSystem()

  def makedirs(self, path):
    self.file_system.makedirs(path)

  def symlink(self, actual_path, link_path):
    self.file_system.symlink(actual_path, link_path)

  def create_file(self, filename):
    self.file_system.createfile(filename)

  def rmtree(self, path):
    self.file_system.rmtree(path)