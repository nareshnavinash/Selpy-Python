from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

class Store:
	drivers = []
	current_driver = None

	def __init__(self):
		print("Storing the driver values")

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
