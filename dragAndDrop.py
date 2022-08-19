from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://ww.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element = driver.find_element(By.XPATH, "//*[@id='box6']")
target_element = driver.find_element(By.XPATH, "//*[@id='box106']")

actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()  # drag and drop

