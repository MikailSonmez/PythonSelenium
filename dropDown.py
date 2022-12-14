from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element(By.ID, "RESULT_RadioButton-9")
drp = Select(element)

# select by_visible_text
drp.select_by_visible_text('Morning')

# select by_visible_index
drp.select_by_index(2)  # Afternoon

# select by_value
drp.select_by_value("Radio-2")  # Evening

# Count number of options
print(len(drp.options))

# Capture all the options and print them as output
all_options = drp.options

for option in all_options:
    print(option.text)
