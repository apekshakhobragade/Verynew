from selenium.webdriver.common.by import By


class DashPage:
    def __init__(self,driver):
        self.driver=driver
        self.dashboard = "//h6[normalize-space()='Dashboard']"

    def dash(self):
        return self.driver.find_element(By.XPATH, self.dashboard).text
