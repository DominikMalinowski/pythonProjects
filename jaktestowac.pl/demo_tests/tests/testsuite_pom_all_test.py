import unittest
from tests.lost_hat_login_page_pom_tests import LostHatLoginPomTest
from tests.lost_hat_home_page_pom_tests import LostHatsFrontPagePomTests
from tests.lost_hat_product_pom_tests import LostHatProductPomTest
from tests.lost_hat_product_details_pom_test import LostHatProductPomTest
from tests.lost_hat_search_page_pom_test import LostHatSearchPomTests
from tests.lost_hat_shopping_cart_pom_tests import LostHatShoppingCartPomTests


def full_suite():
   test_suite = unittest.TestSuite()
   # adding test classes:
   test_suite.addTest(unittest.makeSuite(LostHatLoginPomTest))
   test_suite.addTest(unittest.makeSuite(LostHatsFrontPagePomTests))
   test_suite.addTest(unittest.makeSuite(LostHatProductPomTest))
   test_suite.addTest(unittest.makeSuite(LostHatProductPomTest))
   test_suite.addTest(unittest.makeSuite(LostHatSearchPomTests))
   test_suite.addTest(unittest.makeSuite(LostHatShoppingCartPomTests))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())