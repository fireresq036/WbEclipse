'''
Created on Feb 7, 2013

@author: mrrussell
'''
import unittest
from com.wb.Eclipse import Eclipse

class Test(unittest.TestCase):

  def setUp(self):
    self.eclipse421 = Eclipse()
    self.eclipse421.parseVersion("4.2.1")

  def testCreation(self):
    self.assertEqual("4", self.eclipse421.major())
    self.assertEqual("2", self.eclipse421.minor())
    self.assertEqual("1", self.eclipse421.patch())

  def testFormating(self):
    eclipse421 = Eclipse()
    eclipse421.parseVersion("4.2.1")
    formated = self.eclipse421.fullWithoutDots()
    self.assertEqual("421", formated)
    formated = self.eclipse421.fullWithDots()
    self.assertEqual("4.2.1", formated)
    formated = self.eclipse421.shortWintoutDots()
    self.assertEqual("42", formated)
    formated = self.eclipse421.shortWithDots()
    self.assertEqual("4.2", formated)

if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testCreation']
  unittest.main()