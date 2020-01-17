from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

class Driver:
	driver = None

	def __init__(self,browser = "chrome") -> None:
		if browser == "chrome":
			self.driver = webdriver.Chrome()
		elif browser == "firefox":
			self.driver = webdriver.Firefox()
		elif browser == "safari":
			self.driver = webdriver.Safari()

	def get_driver(self) -> WebDriver:
		return self.driver

	def get(self, url: str) -> None:
		self.driver.get(url)


