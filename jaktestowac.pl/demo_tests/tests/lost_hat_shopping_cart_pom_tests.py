# import of selenium and webdriver
from helpers.base_test_class import BaseTestClass

from helpers.wrappers import screenshot_decorator
from pages.art_category_page import ArtCategoryPage

class LostHatShoppingCartPomTests(BaseTestClass):

    @screenshot_decorator
    def test_adding_item_to_shopping_cart(self):

        expected_text = '\ue876Product successfully added to your shopping cart'
        item_name = "Mountain fox - Vector graphics"

        art_category_page  = ArtCategoryPage(self.conf_driver)
        art_category_page.visit()
        product_page = art_category_page.open_product_page(item_name)
        confirmation_modal_element_text = product_page.add_item_and_get_confirmation_message(item_name)

        self.assertEqual(expected_text, confirmation_modal_element_text)

    @screenshot_decorator
    def test_adding_multiple_item_to_shopping_cart(self):
        expected_cart_products_count_xpath = '(2)'
        item_name = "Mountain fox - Vector graphics"

        art_category_page = ArtCategoryPage(self.conf_driver)
        art_category_page.visit()

        product_page = art_category_page.open_product_page(item_name)
        product_page.add_item_to_cart()
        product_page.add_item_to_cart()

        observed_cart_products_count = product_page.get_items_count()
        self.assertEqual(expected_cart_products_count_xpath, observed_cart_products_count)



