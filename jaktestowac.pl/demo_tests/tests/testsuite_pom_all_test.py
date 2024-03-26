
import unittest

from lost_hat_front_page_pom_tests import LostHatsFrontPagePomTests
from lost_hat_login_page_pom_tests import LostHatLoginPomTest

def full_suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(LostHatsFrontPagePomTests))
    test_suite.addTest(unittest.makeSuite(LostHatLoginPomTest))

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())