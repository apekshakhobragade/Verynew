import pytest
from selenium import webdriver
driver=None
import configparser
config=configparser.ConfigParser()
config.read("Verynew/Utilities/input.properties")


@pytest.fixture
def setup(request):
    global driver
    request.cls.driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    request.cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #request.cls.driver.get(config.get("Url","base_url"))
    yield
    request.cls.driver.quit()
