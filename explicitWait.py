from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

# driver.find_element(By.ID, "tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()  # Flights button

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")  # origin

time.sleep(2)  # from python

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")  # destination

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/10/2018")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("15/10/2018")

driver.find_element(By.XPATH, "flight-departing-hp-flight']/div[7]/label/button").click()  # search

# Explicit waits
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(3)

driver.quit()
