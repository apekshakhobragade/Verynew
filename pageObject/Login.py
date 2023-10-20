from selenium.webdriver.common.by import By


class LoginPage1:
    def __init__(self,driver):
        self.driver=driver
        self.username= "username"
        self.password="password"
        self.button="//button[@type='submit']"
        self.invalid_msg="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def user_input(self,username):
        self.driver.find_element(By.NAME,self.username).send_keys(username)


    def password_input(self,password):
        self.driver.find_element(By.NAME,self.password).send_keys(password)

    def click_button(self):
        self.driver.find_element(By.XPATH,self.button).click()

    def dash(self):
        self.driver.find_element(By.XPATH, self.dashboard).text

    def click_invalidmsg(self):
        self.driver.find_element(By.XPATH, self.invalid_msg).text
