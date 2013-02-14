'''
Created on Feb 7, 2013

@author: mrrussell
'''
import unittest
from com.google.wb.Eclipse import ECLIPSE_420, Eclipse


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

if __name__ == "__main__":
#    import sys;sys.argv = ['', 'Test.testCreation']
    unittest.main()