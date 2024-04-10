import config_reader
from pages.category_page import CategoryPage


class ArtCategoryPage(CategoryPage):
    def __init__(self, driver):
        super().__init__(driver)
        config = config_reader.load()
        self.url = config['base_url'] + '9-art'