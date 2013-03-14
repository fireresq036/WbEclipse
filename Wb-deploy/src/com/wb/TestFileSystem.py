'''
Created on Mar 13, 2013

@author: mrrussell
'''
import os
import shelve

class _CommonObject(object):
  def __init__(self, filename, is_link=False, link_source=None):
    self.name = filename
    self.is_link = is_link
    if self.is_link and link_source is None:
      raise Exception("if link is specified then you must specify a source")
    self.link_source - link_source
  def filename(self):
    return self.name

  def islink(self):
    return self.is_link

  def link_source(self):
    return self.link_source

class _File(_CommonObject):
  def directory(self, directory):
    self.directory = directory

class _Dir(_CommonObject):
  def __init__(self):
    self.elements = []

  def addElement(self, element):
    self.elements.append(element)

  def removeElement(self, element):
    self.elements.remove(element)

  def listElements(self):
    return self.elements

class TestFileSystem(object):
  '''
  fake file system for testing
  '''


  def __init__(self):
    '''
    Constructor
    '''
    self.vfs_store = os.path.join('/', 'tmp', 'vfs.shelve')
    self.vfs = shelve.open(self.vfs_store)
    self.vfs['test'] = 'this is a test'
    self.vfs.close()
    self.vfs = shelve.open(self.vfs_store);
    print "test = " + self.vfs['test']

  def sep(self):
    return os.sep;

  def join(self, *args):
    full_path = ''
    sep = self.sep()
    for element in args:
      full_path += element
      full_path += sep
    return full_path[:-1]

  def listdir(self, dir_path):
    print 'looking up ' + dir_path
    if not self.vfs.has_key(dir_path):
      raise Exception("directory %s not found" % (dir_path))

    directory = self.vfs[dir_path]
    returns = []
    for element in directory.listElements:
      returns.append(element.filename())
    return returns
    
if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testCreation']
  tfs = TestFileSystem()