import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_smoke_tests import LostHatSmokeTest

def smoke_suite():
    test_suite = unittest.TestSuite()

    # adding test classes
    test_suite.addTest(makeSuite(LostHatSmokeTest))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)

runner.run(smoke_suite())