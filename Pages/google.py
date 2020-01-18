from Locators.google import GoogleLocator


class GooglePage(GoogleLocator):

    def __init__(self):
        super().__init__()

    @classmethod
    def enter_search_text(cls, string):
        GoogleLocator.search_box.send_keys(string)

    @classmethod
    def get_search_text(cls) -> str:
        return GoogleLocator.search_box.text()

    @classmethod
    def is_search_box_displayed(cls) -> str:
        return GoogleLocator.search_box.is_displayed_with_wait(10)
