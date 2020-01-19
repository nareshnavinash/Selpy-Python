from selenium import webdriver


class Store:
    drivers = []
    current_driver = None

    @classmethod
    def push(self, driver: webdriver) -> webdriver:
        self.drivers.append(driver)
        self.set_current_driver(driver)

    @classmethod
    def set_current_driver(self, driver: webdriver) -> webdriver:
        self.current_driver = driver

    @classmethod
    def switch_driver(self, driver) -> webdriver:
        self.current_driver = driver
