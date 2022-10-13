import time

import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Config.config import TestData
from TestCase.test_Base import BaseTest


class Test_HomePage(BaseTest):

    def test_HomePage_elements(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        homePage.Click_Admin()
        print("Test Pass")
        time.sleep(3)
