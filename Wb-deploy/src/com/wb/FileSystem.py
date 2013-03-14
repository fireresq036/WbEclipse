'''
Created on Mar 13, 2013

@author: mrrussell
'''

from com.wb.TestFileSystem import TestFileSystem
from com.wb.RealFileSystem import RealFileSystem

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
  
  def join(self, *arg):
    return self.file_system.join()
  
  def readlink(self, path):
    return self.file_system.readlink(path)
  
  def islink(self, path):
    return self.file_system.islink(path)
  
  def listdir(self, dir_path):
    return self.file_system.listdir(dir_path)