import allure
import pytest
from Library.driver import Driver
from Pages.amazon_home_page import AmazonHomePage
from Library.variable import Var


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
        assert (AmazonHomePage.get_selected_category() ==
                static_variable.static_value_for("category")), "Category is not selected properly"

    with allure.step("Search for the text which is needed in this case: " + static_variable.static_value_for("search_text")):
        AmazonHomePage.search_in_the_search_box(static_variable.static_value_for("search_text"))
