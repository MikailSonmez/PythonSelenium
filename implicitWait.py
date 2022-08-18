from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

driver.find_element(By.NAME, "userName").send_keys("mercury")
driver.find_element(By.NAME, "password").send_keys("mercury")

driver.find_element(By.NAME, "login").click()