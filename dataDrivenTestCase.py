from selenium import webdriver
from selenium.webdriver.common.by import By

import XLUtils


driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

path = "D:/Login1.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")

for r in range (2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.NAME, "login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("test is passed")
        XLUtils.writeData(path, "sheet1", r, 3, "test passed")
    else:
        print("test failed")
        XLUtils.writeData(path, "sheet1", r, 3, "test failed")

        driver.find_element(By.LINK_TEXT, "home").click()



