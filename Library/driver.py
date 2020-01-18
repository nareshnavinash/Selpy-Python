from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote import webelement
import os
from Library.store import Store


class Driver:
	driver = None

	def __init__(self, browser = "chrome") -> None:
		if browser == "chrome":
			options = webdriver.ChromeOptions()
			options.add_argument("--no-sandbox")
			options.add_argument("--foreground")
			options.add_argument('disable-infobars')
			options.add_argument("--disable-extensions")
			# options.add_argument("--headless")
			self.driver = webdriver.Chrome(options=options)
			self.driver.implicitly_wait(20)
		elif browser == "firefox":
			self.driver = webdriver.Firefox()
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

	def find_elements(self, by, value) -> list[webelement.WebElement]:
		try:
			return self.driver.find_elements(by, value)
		except NoSuchElementException:
			print("Element not found \n\n" + by + "\n" + value)
		except Exception as e:
			print("Error in finding the element \n\n" + by + "\n" + value + "\nException: \n" + str(e))

	def refresh(self) -> None:
		self.driver.refresh()

	def execute_script(self, script, locator) -> None:
		self.driver.execute_script(self, script, locator)

	def current_url(self) -> str:
		return self.driver.current_url

	def save_screenshot(self) -> bool:
		ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
		CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')
		self.driver.save_screenshot(self, )


	def quit(self):
		self.driver.quit()
