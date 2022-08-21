import time

from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensoruce-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")
        time.sleep(5)
    def test_login(self):
        self.driver.get("https://opensoruce-demo.orangehrmlive.com")
        self.driver.find_element(By.NAME, "txtUsername").clear()
        self.driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.NAME, "txtPassword").clear()
        self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def testDownClass(cls):
        cls.driver.quit()
        print("Test completed......")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\mikai\PycharmProjects\PythonSelenium\\Reports'))
