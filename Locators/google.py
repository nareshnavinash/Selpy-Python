from Library.locator import Locator


class GoogleLocator:
    search_box = Locator("css selector", "input.gLFyf")

    def __init__(self):
        print("Locators for google page")
