import pytest
import allure
import os
from Library.driver import Driver
from Pages.google import GooglePage
from Library.variable import Var


@allure.feature("Google Search")
@allure.step('Enter and search')
@allure.severity('Critical')
def test_google_search():
    with allure.step("Set the test data file needed for this test run"):
        variable = Var("google.yml")

    with allure.step("first step"):
        d = Driver()
        d.get(variable.loc("url"))
        print("landed in google home page")

    with allure.step("second step"):
        GooglePage.enter_search_text(variable.loc("search_text"))


