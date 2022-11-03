
import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_product_tests import LostHatProductTest
from lost_hat_login_tests import LostHatLoginTest
from lost_hats_front_page_tests import LostHatsFrontPageTests
from lost_hat_product_details_tests import LostHatProductDetailsTests

def full_suite():
    test_suite = unittest.TestSuite()

    # adding test classes
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_suite.addTest(unittest.makeSuite(LostHatProductTest))
    test_suite.addTest(unittest.makeSuite(LostHatLoginTest))
    test_suite.addTest(unittest.makeSuite(LostHatsFrontPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatProductDetailsTests))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
