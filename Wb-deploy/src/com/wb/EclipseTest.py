'''
Created on Feb 7, 2013

@author: mrrussell
'''
import unittest
from com.wb.Eclipse import Eclipse
from com.wb.Eclipse import EclipseException

class Test(unittest.TestCase):

  def setUp(self):
    self.eclipse421 = Eclipse()
    self.eclipse431Qualifier = Eclipse()
    self.eclipse421.parseVersion("4.2.1")
    self.eclipse431Qualifier.parseVersion("4.3.1.abcdef")

  def testCreation(self):
    self.assertEqual("4", self.eclipse421.major())
    self.assertEqual("2", self.eclipse421.minor())
    self.assertEqual("1", self.eclipse421.service())
    with self.assertRaises(EclipseException):
      self.eclipse421.qualifier()
    self.assertEqual("4", self.eclipse431Qualifier.major())
    self.assertEqual("3", self.eclipse431Qualifier.minor())
    self.assertEqual("1", self.eclipse431Qualifier.service())
    self.assertEqual("abcdef", self.eclipse431Qualifier.qualifier())

  def testFormatingThreeNumbers(self):
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
    with self.assertRaises(EclipseException):
      self.eclipse421.qualifierWithDots()
    with self.assertRaises(EclipseException):
      self.eclipse421.qualifierWithoutDots()

  def testFormatingFourNumbers(self):
    eclipse = Eclipse()
    eclipse.parseVersion("4.2.1.abcd")
    formated = eclipse.fullWithoutDots()
    self.assertEqual("421", formated)
    formated = eclipse.fullWithDots()
    self.assertEqual("4.2.1", formated)
    formated = eclipse.shortWintoutDots()
    self.assertEqual("42", formated)
    formated = eclipse.shortWithDots()
    self.assertEqual("4.2", formated)
    formated = eclipse.qualifierWithoutDots()
    self.assertEqual("421abcd", formated)
    formated = eclipse.qualifierWithDots()
    self.assertEqual("4.2.1.abcd", formated)

  def testParsingIllegalValues(self):
    eclipse = Eclipse()
    with self.assertRaises(EclipseException):
      eclipse.parseVersion("4")
    with self.assertRaises(EclipseException):
      eclipse.parseVersion("4.2")
    eclipse.parseVersion("4.2.3")
    eclipse.parseVersion("4.2.3.2we3")
    with self.assertRaises(EclipseException):
      eclipse.parseVersion("4.2.3.sdfsre.sdfse.sfd.sdfs")

if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testCreation']
  unittest.main()