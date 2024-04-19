from helpers.base_test_class import BaseTestClass
from helpers.wrappers import screenshot_decorator
from pages.search_page import SearchPage


class LostHatSearchPomTests(BaseTestClass):
    @screenshot_decorator
    def test_sanity_search_on_main_page(self):
        search_phrase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-Shirt'

        search_page = SearchPage(self.conf_driver)
        search_page.visit()
        search_page.search(search_phrase)

        result_elements = search_page.get_search_results()
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1

        self.assertEqual(1, found_elements_number,
                         f"We expect 1 and actual number of found items is {found_elements_number}")
