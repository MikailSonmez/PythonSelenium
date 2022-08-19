from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

element = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

actions.double_click(element).perform()  # double click on button
