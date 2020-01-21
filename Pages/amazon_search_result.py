from Locators.amazon_search_result import AmazonSearchResultLocator


# Inherit the locator class inside page class for easier access of locators
class AmazonSearchResultPage(AmazonSearchResultLocator):

    def __init__(self):
        super().__init__()

    @classmethod
    def is_search_result_page_displayed(cls):
        return AmazonSearchResultLocator.amazon_search_result_top_header.wait_till_displayed()

    @classmethod
    def get_search_result_head_liner_text(cls):
        return AmazonSearchResultLocator.amazon_search_result_top_header.text()

    @classmethod
    def is_filter_set_in_head_liner(cls, string):
        head_liner = AmazonSearchResultLocator.amazon_search_result_top_header.text()
        result = head_liner.find(str(string))
        print("headliner : " + str(head_liner) + " expected string: " + str(string) + " result: " + str(result))
        if result != -1:
            return True
        else:
            return False

    @classmethod
    def select_department(cls, string):
        AmazonSearchResultLocator.amazon_search_result_department_see_more.click()
        AmazonSearchResultLocator.amazon_search_result_department(string).click()

    @classmethod
    def select_sub_department(cls, string):
        AmazonSearchResultLocator.amazon_search_result_department_see_more.click()
        AmazonSearchResultLocator.amazon_search_result_department(string).click()

    @classmethod
    def select_average_customer_review(cls, string):
        AmazonSearchResultLocator.amazon_search_avg_customer_review(string).click()

    @classmethod
    def set_sort_by(cls, string):
        AmazonSearchResultLocator.amazon_search_sort_by.click()
        AmazonSearchResultLocator.amazon_search_sort_by_selector(string).wait_till_displayed()
        AmazonSearchResultLocator.amazon_search_sort_by_selector(string).click()

    @classmethod
    def set_min_max_price(cls, min_price, max_price):
        AmazonSearchResultLocator.amazon_search_price_min.send_keys(min_price)
        AmazonSearchResultLocator.amazon_search_price_max.send_keys(max_price)
        AmazonSearchResultLocator.amazon_search_price_go.click()

    @classmethod
    def select_checkbox_filter(cls, string):
        AmazonSearchResultLocator.amazon_search_checkbox_filters(string).move_and_click()

    @classmethod
    def select_a_product_from_search_result(cls, number):
        AmazonSearchResultLocator.amazon_search_result_list_header(number).click()
