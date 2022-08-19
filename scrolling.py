from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()  # maximize window size

# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,1000)", "")

# 2. Scroll down page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Turkey']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# 3. Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
