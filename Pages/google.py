from Locators.google import GoogleLocator


class GooglePage(GoogleLocator):

    def __init__(self):
        super

    @classmethod
    def enter_search_text(cls, string):
        GoogleLocator.search_box.send_keys(string)

