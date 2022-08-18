from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# How to find how many input boxes present in web page

inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))  # 6

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Displayed or not", status)

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Enable or not", status)

# How to provide value into text box

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("mikail")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("sonmez")

driver.find_element(By.ID, 'RESULT_TextField-3').send_keys("333333333")
