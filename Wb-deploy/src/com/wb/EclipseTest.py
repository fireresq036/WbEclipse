'''
Created on Feb 7, 2013

@author: mrrussell
'''
import unittest
from com.wb.Eclipse import Eclipse

class Test(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testCreation(self):
    eclipse421 = Eclipse()
    eclipse421.parseVersion("4.2.1")
    eclipse421.displayFull()
    self.assertEqual("4", eclipse421.major())
    self.assertEqual("2", eclipse421.minor())
    self.assertEqual("1", eclipse421.patch())

  def testFormating(self):
    eclipse421 = Eclipse()
    eclipse421.parseVersion("4.2.1")
    formated = eclipse421.fullWithoutDots()
    self.assertEqual("421", formated)
    formated = eclipse421.fullWithDots()
    self.assertEqual("4.2.1", formated)
    formated = eclipse421.shortWintoutDots()
    self.assertEqual("42", formated)
    formated = eclipse421.shortWithDots()
    self.assertEqual("4.2", formated)

if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testCreation']
  unittest.main()