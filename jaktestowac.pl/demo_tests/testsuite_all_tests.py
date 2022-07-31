
import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_smoke_tests import LostHatSmokeTest
from lost_hat_product_tests import LostHatProductTest
from lost_hat_login_tests import LostHatLoginTest
from lost_hats_front_page_tests import LostHatsFrontPageTests

def full_suite():
    test_suite = unittest.TestSuite()

    # adding test classes
    test_suite.addTest(makeSuite(LostHatSmokeTest))
    test_suite.addTest(makeSuite(LostHatProductTest))
    test_suite.addTest(makeSuite(LostHatLoginTest))
    test_suite.addTest(makeSuite(LostHatsFrontPageTests))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)
runner.run(full_suite())
