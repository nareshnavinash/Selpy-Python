import pytest
from Library.driver import Driver

def test_file1_method1():
	d = Driver("chrome")
	d.get("https://www.google.com")
	dr = d.get_driver()
	print(dr)
	x=5
	y=6
	assert x+1 == y,"test failed"
	# assert x == y,"test failed"
