import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")

print(driver.title)  # FR

driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)

print(driver.title)  # TT

driver.back()

time.sleep(5)

print(driver.title)  # FR

driver.forward()

print(driver.title)  # TT

driver.close()

