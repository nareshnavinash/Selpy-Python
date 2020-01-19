from Locators.amazon_home_page import AmazonHomePageLocator


class AmazonHomePage(AmazonHomePageLocator):

    def __init__(self):
        super().__init__()

    @classmethod
    def is_home_page_displayed(cls):
        return AmazonHomePageLocator.amazon_logo.is_displayed_with_wait()

    @classmethod
    def select_category_drop_down(cls, string):
        AmazonHomePageLocator.amazon_search_categories.wait_till_displayed()
        AmazonHomePageLocator.amazon_search_categories.select(string)

    @classmethod
    def get_selected_category(cls):
        return AmazonHomePageLocator.amazon_search_categories_text.text()

    @classmethod
    def search_in_the_search_box(cls,string):
        AmazonHomePageLocator.amazon_search_textbox.send_keys(string)
