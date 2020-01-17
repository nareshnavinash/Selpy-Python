import pytest
import allure
import os
from Library.driver import Driver
from Pages.google import GooglePage


@allure.feature("Google Search")
@allure.step('Enter and search')
@allure.severity('Critical')
def test_google_search():
    with allure.step("first step"):
        print(os.environ['BROWSER'])
        d = Driver("chrome")
        d.get("https://www.google.com")
        print("landed in google home page")

    with allure.step("second step"):
        GooglePage.enter_search_text("hello")
        d.quit()


@allure.feature("Google Search 2")
@allure.step('Enter and search 2')
@allure.severity('Critical')
def test_google_search2():
    with allure.step("first step 2"):
        d = Driver("chrome")
        d.get("https://www.google.com")
        print("landed in google home page")

    with allure.step("second step 2"):
        GooglePage.enter_search_text("hello")
        d.quit()
