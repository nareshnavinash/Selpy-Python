import allure
import pytest
import time
from selpy.driver import Driver
from Pages.amazon_home_page import AmazonHomePage
from Pages.amazon_search_result import AmazonSearchResultPage
from Pages.amazon_product_page import AmazonProductPage
from selpy.variable import Var


@allure.feature("Amazon - Book search with text 'AI', department as 'Arts, Film & Photography', sub-department as "
                "'Cinema & Broadcast', maximum 'Avg Customer Review', sort result by 'Publication Date'"
                "filter as 1000 to 1500 rupees, the book available in paperback, Kindle ebooks, and Hardcover"
                "select the first result and verify")
@allure.severity('Critical')
@pytest.mark.regression
@pytest.mark.ui
def test_amazon_book_search_001():
    with allure.step("Initialize the UI dynamic data"):
        ui_dynamic_data = {}
    with allure.step("Set the test data file needed for this test run"):
        static_variable = Var("amazon.yml", "static")
        dynamic_variable = Var("amazon_book_search_result_dynamic.yml", "dynamic")

    with allure.step("Initialize the driver and navigate to the url"):
        driver = Driver()
        driver.get(static_variable.static_value_for("url"))
        assert (AmazonHomePage.is_home_page_displayed() is True), "Amazon home page is not displayed"

    with allure.step("Select the categories as books in the search dropdown"):
        AmazonHomePage.select_category_drop_down(static_variable.static_value_for("category"))
        assert (AmazonHomePage.get_selected_category() == static_variable.static_value_for("category")),\
            "Category is not selected properly"

    with allure.step("Search for the text which is needed in this"):
        search_text = static_variable.static_value_for("search_text")
        AmazonHomePage.search_in_the_search_box(search_text)
        assert (AmazonSearchResultPage.is_search_result_page_displayed() is True), "Search result page is not displayed"
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(search_text) is True), "Searched text is not " \
                                                                                          "displayed in the result page"

    with allure.step("Apply the filter categories in the search results page"):
        AmazonSearchResultPage.select_department(static_variable.static_value_for("search_department"))
        AmazonSearchResultPage.select_sub_department(static_variable.static_value_for("search_sub_department"))
        list_of_checkbox = static_variable.static_value_for("book_format")
        size_of_list = len(list_of_checkbox)
        for book_format in list_of_checkbox:
            AmazonSearchResultPage.select_checkbox_filter(book_format)
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(
            "Format: %s selected" % size_of_list)), "Applied checkbox filter is not listed in the result page headliner"
        AmazonSearchResultPage.select_average_customer_review(static_variable.static_value_for("avg_customer_review"))
        AmazonSearchResultPage.set_sort_by(static_variable.static_value_for("sort_by"))
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(
            static_variable.static_value_for("search_department")) is True), "Searched department is not displayed " \
                                                                             "in result page head liner"
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(
            static_variable.static_value_for("search_sub_department")) is True), "Searched sub department is not " \
                                                                                 "displayed in result page head liner"
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(
            static_variable.static_value_for("avg_customer_review")) is True), "Avg customer review is not displayed " \
                                                                               "in result page head liner"
        AmazonSearchResultPage.set_min_max_price(static_variable.static_value_for("min_price"),
                                                 static_variable.static_value_for("max_price"))
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(
            static_variable.static_value_for("min_price")) is True), "min_price is not displayed in result page head " \
                                                                     "liner "
        assert (AmazonSearchResultPage.is_filter_set_in_head_liner(
            static_variable.static_value_for("max_price")) is True), "max_price is not displayed in result page head " \
                                                                     "liner "

    with allure.step("Select a product from the search result page"):
        AmazonSearchResultPage.select_a_product_from_search_result(static_variable.static_value_for("select_product"))
        assert (driver.window_handles_count() == 2), "New tab is not opened after clicking a product"
        driver.switch_to_new_tab()
        assert (AmazonProductPage.is_product_page_displayed() is True), "Product page is not displayed after selecting"

    with allure.step("Set the delivery pincode in the product page"):
        AmazonProductPage.set_delivery_pincode(static_variable.static_value_for("delivery_pincode"))
        for i in range(0, 10):
            time.sleep(1)
            res = AmazonProductPage.get_delivery_pincode().find(
                str(static_variable.static_value_for("delivery_pincode")))
            if res != -1:
                break
        print("pincode: " + AmazonProductPage.get_delivery_pincode())
        assert (res != -1), "Delivery Pin code is not set properly"

    with allure.step("Store the UI details in the dynamic dictionary"):
        AmazonProductPage.amazon_product_title.scroll_to_locator()
        ui_dynamic_data["amazon_product_title"] = AmazonProductPage.amazon_product_title.texts_as_string()
        AmazonProductPage.amazon_product_byline_info.scroll_to_locator()
        ui_dynamic_data["amazon_product_byline_info"] = AmazonProductPage.amazon_product_byline_info.texts_as_string()
        AmazonProductPage.amazon_product_formats.scroll_to_locator()
        ui_dynamic_data["amazon_product_formats"] = AmazonProductPage.amazon_product_formats.texts_as_string()
        driver.switch_to_frame(AmazonProductPage.amazon_product_detail_description_iframe.get_element())
        ui_dynamic_data["amazon_product_detail_description"] = AmazonProductPage.\
            amazon_product_detail_description.texts_as_string()
        driver.switch_to_default_content()
        AmazonProductPage.amazon_product_offers.scroll_to_locator()
        ui_dynamic_data["amazon_product_offers"] = AmazonProductPage.amazon_product_offers.texts_as_string()
        AmazonProductPage.amazon_product_description.scroll_to_locator()
        ui_dynamic_data["amazon_product_description"] = AmazonProductPage.amazon_product_description.texts_as_string()
        AmazonProductPage.amazon_product_details.scroll_to_locator()
        ui_dynamic_data["amazon_product_details"] = AmazonProductPage.amazon_product_details.texts_as_string()

    with allure.step("Compare the dynamic value from UI with the stored file"):
        dynamic_variable.compare(ui_dynamic_data)
