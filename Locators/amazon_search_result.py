from selpy.locator import Locator


class AmazonSearchResultLocator:
    amazon_search_result_top_header = Locator("css selector", "div.sg-col-inner div.a-section")
    amazon_search_result_department_see_more = Locator("css selector", "div#departments span.a-expander-prompt")
    amazon_search_sort_by = Locator("css selector", "span.a-dropdown-container")
    amazon_search_price_min = Locator("css selector", "div#priceRefinements input[placeholder='Min']")
    amazon_search_price_max = Locator("css selector", "div#priceRefinements input[placeholder='Max']")
    amazon_search_price_go = Locator("css selector", "div#priceRefinements span.a-button")

    def __init__(self):
        print("Locators for Amazon search result page page")

    @classmethod
    def amazon_search_result_department(cls, string):
        return Locator("xpath", "//div[@id='departments']//li[contains(@class,'a-spacing-micro')]"
                                "//span[text()='%s']" % string)

    # For average customer review use the following strings for respective avg cust review
    # 4 Stars & Up
    # 3 Stars & Up
    # 2 Stars & Up
    # 1 Star & Up
    @classmethod
    def amazon_search_avg_customer_review(cls, string):
        return Locator("css selector", "div#reviewsRefinements section[aria-label='%s']" % string)

    @classmethod
    def amazon_search_sort_by_selector(cls, string):
        return Locator("xpath", "//div[contains(@class,'a-popover-inner')]//a[text()='%s']" % string)

    @classmethod
    def amazon_search_checkbox_filters(cls, string):
        return Locator("xpath", "//ul[contains(@class,'a-unordered-list')]//span[text()='%s']" % string)

    @classmethod
    def amazon_search_result_list_header(cls, number):
        return Locator("xpath", "((//div[contains(@class,'s-result-list')]//div"
                                "[contains(@class,'s-include-content-margin')])[%s]//div"
                                "[contains(@class,'sg-col-4-of-12')]//div[@class='sg-row']//span)[1]" % number)
