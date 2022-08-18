import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()

time.sleep(5)

# Alert(driver).accept()  # classes alert window using OK button

Alert(driver).accept()  # classes alert window using CANCEL button
