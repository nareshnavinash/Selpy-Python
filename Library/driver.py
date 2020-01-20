from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote import webelement
from Library.variable import Var
from Library.store import Store


class Driver:
    driver = None
    current_window_handle = None

    def __init__(self) -> None:
        if not Var.env("browser") == "None":
            browser = Var.env("browser")
        else:
            browser = Var.glob("browser")
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--foreground")
            options.add_argument('disable-infobars')
            options.add_argument("--disable-extensions")
            if str(Var.glob("headless")) == "1" or str(Var.env("headless")) == "1":
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            self.driver.implicitly_wait(int(Var.glob("implicit_wait")))
            self.driver.set_window_size(int(Var.glob("browser_horizontal_size")),
                                        int(Var.glob("browser_vertical_size")))
        elif browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "safari":
            self.driver = webdriver.Safari()
        Store.push(self.driver)

    def get(self, url: str) -> None:
        self.driver.get(url)

    def find_element(self, by, value) -> webelement.WebElement:
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            print("Element not found \n\n" + by + "\n" + value)
        except Exception as e:
            print("Error in finding the element \n\n" + by + "\n" + value + "\nException: \n" + str(e))

    def find_elements(self, by, value):
        try:
            return self.driver.find_elements(by, value)
        except NoSuchElementException:
            print("Element not found \n\n" + by + "\n" + value)
        except Exception as e:
            print("Error in finding the element \n\n" + by + "\n" + value + "\nException: \n" + str(e))

    def refresh(self) -> None:
        self.driver.refresh()

    def execute_script(self, script, *args) -> None:
        self.driver.execute_script(self, script, *args)

    def current_url(self) -> str:
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

    def switch_to_new_tab(self):
        self.current_window_handle = self.driver.current_window_handle
        list_of_window_handles = self.driver.window_handles
        list_of_window_handles.remove(self.current_window_handle)
        self.driver.switch_to.window(list_of_window_handles.pop())

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def window_handles_count(self):
        return len(self.driver.window_handles)

    def switch_to_parent_tab(self):
        self.driver.switch_to.window(self.current_window_handle)

    def close_current_tab(self):
        self.driver.close()
