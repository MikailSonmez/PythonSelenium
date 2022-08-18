from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with the radio buttons

status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()  # true/false
print(status)

driver.find_element(By.ID, "RESULT_RadioButton-7_0").click()  # select radio button

status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()  # true/false
print(status)

# Working with check boxes

driver.find_element(By.ID, "RESULT_CheckBox-8_0").click()  # sunday
driver.find_element(By.ID, "RESULT_CheckBox-8_6").click()  # saturday

status = driver.find_element(By.ID, "RESULT_CheckBox-8_0").is_selected()
print(status)
