from Library.store import Store


class Locator(Store):

    def __init__(self, by: str, value: str) -> None:
        self.by = by
        self.value = value

    def send_keys(self, string) -> None:
        Store.current_driver.find_element(self.by, self.value).send_keys(string)
