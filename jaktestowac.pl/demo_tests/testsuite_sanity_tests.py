import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_login_tests import LostHatLoginTest

def sanity_suite():
    test_suite = unittest.TestSuite()

    # adding test classes
    test_suite.addTest(LostHatLoginTest('test_correct_login'))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)

runner.run(sanity_suite())
