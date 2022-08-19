import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies have been created
print(cookies)  # print all the cookie pairs

# Adding new cookie to the browser
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after adding new cookie
print(cookies)  # print all the cookie pairs

# Deleting cookie
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after deleting new cookie

# Deleting all cookies
driver.delete_all_cookies()  # deletes all cookies
cookies = driver.get_cookies()  # capture all the cookies after deletes all
print(len(cookies))  # 0


