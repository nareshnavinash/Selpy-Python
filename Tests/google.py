import allure
from Library.driver import Driver
from Pages.google import GooglePage
from Library.variable import Var


@allure.feature("Google Search")
@allure.severity('Critical')
def test_google_search():
    dynamic_data = {}
    with allure.step("Set the test data file needed for this test run"):
        variable = Var("google.yml", "local")
        dynamic_var = Var("dyn_google.yml", "dynamic")

    with allure.step("first step"):
        d = Driver()
        d.get(variable.local_value_for("url"))
        print("landed in google home page")

    with allure.step("second step"):
        assert (GooglePage.is_search_box_displayed() is True)
        GooglePage.enter_search_text(variable.local_value_for("search_text"))
        dynamic_data["search_text"] = GooglePage.get_search_text()
        dynamic_data["name"] = GooglePage.search_box.get_attribute("name")
        dynamic_data["type"] = GooglePage.search_box.get_attribute("type")
        dynamic_var.compare(dynamic_data)
