import unittest
from unittest import TextTestRunner, makeSuite, TestSuite

from lost_hat_smoke_test import LostHatSmokeTests

def smoke_suite():
    test_suite = unittest.TestSuite()

    # adding test classes
    test_suite.addTest(makeSuite(LostHatSmokeTests))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)

runner.run(smoke_suite())
