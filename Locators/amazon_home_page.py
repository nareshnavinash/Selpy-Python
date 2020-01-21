from selpy.locator import Locator


class AmazonHomePageLocator:
    amazon_logo = Locator("css selector", "div#nav-logo a[aria-label='Amazon']")
    amazon_search_categories = Locator("css selector", "div.nav-search-scope select.nav-search-dropdown")
    amazon_search_categories_text = Locator("css selector", "div.nav-search-facade span")
    amazon_search_textbox = Locator("css selector", "div.nav-search-field input.nav-input")
    amazon_search_button = Locator("css selector", "div.nav-search-submit")

    def __init__(self):
        print("Locators for Amazon home page")

    @staticmethod
    def amazon_search_category_list(string):
        amazon_search_category_list = Locator("xpath", "//select[contains(@class,'nav-search-dropdown')]//option[text("
                                                       ")='%s']" % string)
        return amazon_search_category_list
