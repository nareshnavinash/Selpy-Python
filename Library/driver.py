from selenium import webdriver
from selenium.webdriver.remote import webelement
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
		return self.driver.find_element(by, value)

	def quit(self):
		self.driver.quit()


