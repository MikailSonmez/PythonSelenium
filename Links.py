from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")

print("Number of links present:", len(links))  # print how many links present in a page

for link in links:
    print(link.text)

# clicking on the link

# driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()
