import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\Users\mikai\Downloads")
fp.set_preference("browser.download.folferList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(firefox_profile=fp)

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
