from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element(By.NAME, "userName")
print(user_ele.is_displayed())  # returns true/false based of element status
print(user_ele.is_enabled())  # returns true/false

pwd_ele = driver.find_element(By.NAME, "password")
print(pwd_ele.is_displayed())  # returns true/false based of element status
print(pwd_ele.is_enabled())  # returns true/false

driver.find_element(By.NAME, "login").click()

roundtrip_radio = driver.find_element(By.CSS_SELECTOR, "input[value=roundtrip]")
print("status of round trip radio button", roundtrip_radio.is_selected())  # print status of radio button round trip

onetrip_radio = driver.find_element(By.CSS_SELECTOR, "input[value=oneway")
print("status of one way radio button", onetrip_radio.is_selected())

