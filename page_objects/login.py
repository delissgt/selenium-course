from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login():
    URL = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    INPUT_USERNAME = (By.XPATH, '//*[@id="login"]/div/div/div[2]/form/div[1]/div[1]/div/div/input')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="login"]/div/div/div[2]/form/div[1]/div[2]/div/div/input')

    INPUT_USERNAME_LOGIN = (By.ID, 'txt-username')
    INPUT_PASSWORD_LOGIN = (By.ID, 'txt-password')

    BUTTON_LOGIN = (By.ID, 'btn-login')


    def __init__(self, driver: webdriver.Chrome):
        self.timeout = 5
        self.driver = driver

    def get_username_value(self):
        return self.driver.find_element(*self.INPUT_USERNAME).get_attribute('value')

    def get_password_value(self):
        return self.driver.find_element(*self.INPUT_PASSWORD).get_attribute('value')

    def set_username_login_value(self):
        self.driver.find_element(*self.INPUT_USERNAME_LOGIN).send_keys('John Doe')

    def set_password_login_value(self):
        self.driver.find_element(*self.INPUT_PASSWORD_LOGIN).send_keys('ThisIsNotAPassword')

    def button_login_click(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()

