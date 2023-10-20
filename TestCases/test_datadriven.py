from selenium import webdriver
import pytest
import time
from Verynew.pageObject.Login import LoginPage1
from Verynew.Utilities.Logger import  Logcls
from Verynew.pageObject.Dashboard import DashPage
from Verynew.Utilities.excelmethod import ExcelMethods

sheet_name='Logindata'
import configparser
config = configparser.ConfigParser()
config.read("Verynew//Utilities//input.properties")

@pytest.mark.usefixtures("setup")
class TestLoginPage2(Logcls):
    @pytest.mark.parametrize("s_no,username,password,condition",ExcelMethods('Logindata').get_parametrize_list())
    def test_set001(self,s_no,username,password,condition):
        log=self.getthelog()

        lg=LoginPage1(self.driver)
        dsh=DashPage(self.driver)
        time.sleep(2)
        log.info("Test the login with correct username and password")
        log.info("Testcase 1")
        log.info("Test case is STARTING")
        lg.user_input(username)
        time.sleep(2)
        log.info("entered username")
        lg.password_input(password)
        log.info("entered password")
        lg.click_button()
        log.info("clicked login button")
        time.sleep(2)
        if condition == "positive":
            if 'Dashboard' in dsh.dash():

                log.info("Testcase Passed")
                status= True
            else:
                self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\pratice_sessionVerynew\\Screen1\\test_set001.png")
                log.critical("Test Case Failed")
                status= False
        elif condition == "negative":
            if 'Invalid credentials' in lg.click_invalidmsg():
                status = True
                log.info("Testcase Passed")
            else:
                self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\pratice_sessionVerynew\\Screen1\\test_set002.png")
                log.critical("Test Case Failed")
                status= False

        ExcelMethods(sheet_name).update_result_in_excel(s_no,status)
        assert status
        time.sleep(12)

