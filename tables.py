from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/mikai/hey.html")

rows = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr"))  # count number of rows
cols = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th"))  # count number of columns

print(rows)
print(cols)

print("Product"+"   "+"Article"+"   "+"Price")

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='   ')  # Product1  0001  10
    print()

