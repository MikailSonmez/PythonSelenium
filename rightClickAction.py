from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)

actions.context_click(button).perform()  # mouse right click action
