from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[1]").send_keys("Admin")
driver.find_element(By.XPATH, "/(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
usermgnt = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()



