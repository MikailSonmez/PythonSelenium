import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/mercurywelcome.php")

# driver.save_screenshot("D:/ScreenShoots/homePage.png")

driver.get_screenshot_as_file("D:/ScreenShoots/homePage2.jpg")

