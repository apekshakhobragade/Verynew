from selenium import webdriver
import pytest
import time
from Verynew.pageObject.Login import LoginPage1
from Verynew.Utilities.Logger import  Logcls
from Verynew.pageObject.Dashboard import DashPage


import configparser
config = configparser.ConfigParser()
config.read("Verynew//Utilities//input.properties")

@pytest.mark.usefixtures("setup")
class TestLoginPage(Logcls):
    def test_set001(self):
        log=self.getthelog()

        lg=LoginPage1(self.driver)
        dsh=DashPage(self.driver)
        time.sleep(2)
        log.info("Testcase 1")
        log.info("Test case is STARTING")
        lg.user_input('Admin')
        time.sleep(2)
        log.info("entered username")
        lg.password_input('admin123')
        log.info("entered password")
        lg.click_button()
        log.info("clicked login button")
        time.sleep(2)
        if 'Dashboard1' in dsh.dash():
            assert True
            log.info("Testcase Passed")
        else:
            self.driver.save_screenshot("Verynew\\Screen1\\test_set001.png")
            log.critical("Test Case Failed")
            assert False
        time.sleep(12)


