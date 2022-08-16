from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver=webdriver.Ie()

# driver=webdriver.Firefox()

driver.get("http://newtours.demoaut.com")

print(driver.title)  # title of the page

print(driver.current_url)  # return the URL of the page

print(driver.page_source)  # HTML code for the page

driver.close()  # close the browser
