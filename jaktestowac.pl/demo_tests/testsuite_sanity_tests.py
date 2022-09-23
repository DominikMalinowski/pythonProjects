import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_login_tests import LostHatLoginTest
from lost_hat_sanity_tests import LostHatSanityTest

def sanity_suite():
    test_suite = unittest.TestSuite()

    # adding test classes
    test_suite.addTest(LostHatLoginTest('test_correct_login'))
    test_suite.addTest(LostHatSanityTest('test_is_searching_bar_working'))

    return test_suite

runner = unittest.TextTestRunner(verbosity=2)

runner.run(sanity_suite())