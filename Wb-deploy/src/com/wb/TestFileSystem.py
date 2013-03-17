'''
Created on Mar 13, 2013

@author: mrrussell
'''
import os
import random
import shelve

class _CommonObject(object):
  def __init__(self, filename, is_link=False, link_source=None):
    self.name = filename
    self.is_link = is_link
    if self.is_link and link_source is None:
      raise Exception('CommonObject: if link is specified then you'
                      ' must specify a source')
    self.link_source = link_source
    self.FILE = 1
    self.DIRECTORY = 2

  def filename(self):
    return self.name

  def islink(self):
    return self.is_link

  def link_source(self):
    return self.link_source

  def type(self):
    pass

class _File(_CommonObject):
  def directory(self, directory):
    self.directory = directory

  def type(self):
    return self.FILE

  def _str(self):
    file_ret = 'File: ' + self.filename()
    if self.is_link:
      file_ret = '{} -> {}'.format(self.link_source, file_ret)
    return file_ret;

class _Dir(_CommonObject):
  def __init__(self, filename, is_link=False, link_source=None):
    self.elements = []
    super(_Dir, self).__init__(filename, is_link, link_source)

  def addElement(self, element):
    self.elements.append(element)

  def removeElement(self, element):
    self.elements.remove(element)

  def listElements(self):
    return self.elements

  def type(self):
    return self.DIRECTORY

  def _str(self):
    dir_ret = 'Dir: ' + self.filename()
    if self.is_link:
      dir_ret = '{} -> {}'.format(self.link_source, dir_ret)
    dir_ret = dir_ret + '('
    if not self.elements:
      dir_ret = dir_ret + 'nothing'
    else:
      for elem in self.elements:
        dir_ret = '{}{}, '.format(dir_ret, elem.filename())
    dir_ret = dir_ret + ')'
    return dir_ret;


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
    for key in self.vfs.keys():
      del self.vfs[key]
    self.root_key = self.sep()
    self.vfs[self.root_key] = _Dir(self.sep())
    self.tmp_dir_key = self.sep() + 'tmp'
    self.vfs[self.tmp_dir_key] = _Dir(self.tmp_dir_key)

  def sep(self):
    return os.sep;

  def listdir(self, dir_path):
    print 'looking up ' + dir_path
    dir_path = self._resolveLinks(dir_path)
    if not self.vfs.has_key(dir_path):
      print "***+++***_++++"
      self._dumpFileSystem()
      raise Exception('listdir: directory {} not found'.format(dir_path))

    directory = self.vfs[dir_path]
    returns = []
    for element in directory.listElements():
      returns.append(element.filename())
    return returns

  def _resolveLinks(self, path):
    path_parts = self._getPathParts(path)
    full_path = ''
    for path in path_parts:
      full_path = full_path + self.sep() + path
      if self.vfs.has_key(full_path):
        fs_element = self.vfs[full_path]
        if fs_element.islink():
          print '{} is a link to {}'.format(full_path, fs_element.link_source)
          full_path = fs_element.link_source
      else:
        raise Exception('_resolveLinks: can not find ' + full_path)
    return full_path

  def _getPathParts(self, path):
    if path[0] != self.sep():
      raise Exception('_getPathParts: paths must start with ' + self.sep())
    else:
      path = path[1:]
    return path.split(self.sep())

  def mkdtemp(self, prefix, suffix, directory):
    tmp_dir = self.vfs[self.tmp_dir_key]
    new_tmp_dir = os.path.join(tmp_dir.filename(), 
                               '{0}{1:05d}{2}'.format(prefix,
                                                      random.randint(10,99999),
                                                      suffix))
    self.vfs[new_tmp_dir] = _Dir(new_tmp_dir)
    tmp_dir.addElement(self.vfs[new_tmp_dir])
    self.vfs[self.tmp_dir_key] = tmp_dir
    return self.vfs[new_tmp_dir].filename()

  def _dumpFileSystem(self):
    print 20 * '*'
    print 'dumping File System'
    print 20 * '*'
    for key in self.vfs.keys():
      print '{} = {}'.format(key, self.vfs[key]._str())
    print 20 * '*'

  def makedirs(self, path_in):
    print 'mkdirs: ' + path_in
    path_parts = self._getPathParts(path_in)
    full_path = ''
    parent_element = self.vfs[self.root_key]
    for path in path_parts:
      full_path = full_path + self.sep() + path
      if self.vfs.has_key(full_path):
        existing_element = self.vfs[full_path]
        parent_key = full_path
        parent_element = existing_element
        if existing_element.type() != existing_element.DIRECTORY:
          raise Exception('makedirs: {} is not a directory'.format(full_path))
      else:
        new_element = _Dir(full_path)
        parent_element.addElement(new_element)
        self.vfs[parent_key]=parent_element
        self.vfs[full_path] = new_element
        parent_element = new_element
        parent_key = full_path

  def symlink(self, actual_path, link_path):
    print 'creating {} -> {}'.format(actual_path, link_path)
    new_element = None
    actual = self.vfs[actual_path]
    if actual.type() == actual.DIRECTORY:
      new_element = _Dir(link_path, True, actual_path)
    else:
      new_element = _File(link_path, True, actual_path)
    self.vfs[link_path] = new_element
    self._addToParent(link_path, new_element)


  def _addToParent(self, path, new_element):
    index = path.rfind(self.sep())
    parent_dir = path[:index]
    parent_element = self.vfs[parent_dir]
    parent_element.addElement(new_element)
    self.vfs[parent_element.filename()]=parent_element


  def createfile(self, filename):
    print "creating file: " + filename
    new_element = _File(filename)
    self._addToParent(filename, new_element)
    self.vfs[filename] = new_element


  def rmtree(self, path):
    for key in self.vfs.keys():
      if path in key:
        del self.vfs[key]

  def islink(self, path):
    return self.vfs[path].islink()

  def readlink(self, path):
    element_link = self.vfs[path]
    if not element_link.islink():
      raise Exception('readlink: {} is not a symlink'.formea(path))
    return element_link.link_source

if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testCreation']
  tfs = TestFileSystem()
  