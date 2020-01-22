from selpy.locator import Locator
# Importing the locator method from selpy


class AmazonHomePageLocator:
    # Use the following description for different locators
    # CSS - 'css selector'
    # XPATH - 'xpath'
    # ID - 'id'
    # NAME - 'name'
    # LINK TEXT - 'link text'
    # PARTIAL LINK TEXT - 'partial link text'
    # TAG NAME - 'tag name'
    # CLASS NAME - 'class name'
    amazon_logo = Locator("css selector", "div#nav-logo a[aria-label='Amazon']")
    # In chrome amazon_search_categories works fine for select
    # In firefox we have an open issue with the
    amazon_search_categories = Locator("css selector", "div.nav-search-scope select.nav-search-dropdown")
    amazon_search_categories_text = Locator("css selector", "div.nav-search-facade span")
    amazon_search_textbox = Locator("css selector", "div.nav-search-field input.nav-input")
    amazon_search_button = Locator("css selector", "div.nav-search-submit")

    def __init__(self):
        print("Locators for Amazon home page")

    # Dynamic locators can be declared as a method with variables.
    @staticmethod
    def amazon_search_category_list(string):
        amazon_search_category_list = Locator("xpath", "//select[contains(@class,'nav-search-dropdown')]//option[text("
                                                       ")='%s']" % string)
        return amazon_search_category_list
