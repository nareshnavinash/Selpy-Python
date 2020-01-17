from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from Library.store import Store

class Driver:
	driver = None

	def __init__(self,browser = "chrome") -> None:
		if browser == "chrome":
			self.driver = webdriver.Chrome()
		elif browser == "firefox":
			self.driver = webdriver.Firefox()
		elif browser == "safari":
			self.driver = webdriver.Safari()
		Store.push(self.driver)

	def get(self, url: str) -> None:
		self.driver.get(url)

	def find_element(self, by, value) -> webelement.WebElement:
		return self.driver.find_element(by, value)


