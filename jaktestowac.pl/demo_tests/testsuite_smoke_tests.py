import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_smoke_tests import LostHatTest

def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatTest))
