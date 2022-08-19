import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chromeOptions = Options()

chromeOptions.add_experimental_option("pref", {"download.default_directory": "C:\Users\mikai\Downloads"})

driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get("https://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

# Download text file

driver.find_element(By.ID, "textbox").send_keys("testing download text file")
driver.find_element(By.ID, "createTxt").click()  # generate file button
driver.find_element(By.ID, "link-to-download").click()  # download link

# Download pdf file

driver.find_element(By.ID, "pdfbox").send_keys("testing pdf")
driver.find_element(By.ID, "createPdf").click()  # generate pdf button
driver.find_element(By.ID, "pdf-link-to-download").click()  # download link

driver.close()
