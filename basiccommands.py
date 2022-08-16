from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")

print(driver.title)  # returns the title of the page
driver.current_url  # return URL
