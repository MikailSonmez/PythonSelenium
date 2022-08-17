import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")

print(driver.title)  # returns the title of the page
print(driver.current_url)  # return URL

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

time.sleep(5)

# driver.close() # crrently focussed browser

driver.quit()  # closes all the browsers
