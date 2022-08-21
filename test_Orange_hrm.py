import time
import pytest
from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By


class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(15)
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title == "OrangeHRM"




