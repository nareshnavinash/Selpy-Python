import pytest
from Library.driver import Driver
from Library.locator import Locator
from Pages.google import GooglePage


def test_file1_method1():
    d = Driver("chrome")
    d.get("https://www.google.com")
    GooglePage.enter_search_text("hello")
