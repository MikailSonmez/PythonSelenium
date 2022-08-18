from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[1]").click()

print(driver.current_window_handle)  # CDwindow-4DA1DD8F016784009FA5EC3D43635EEA

handles = driver.window_handles  # returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()  # close only parent browser

driver.quit()

