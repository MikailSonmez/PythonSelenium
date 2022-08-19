import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000)", "")

driver.switch_to.frame(0)

driver.find_element(By.NAME, "RESULT_FileUpload-10").send_keys("D://thisinit.png")
