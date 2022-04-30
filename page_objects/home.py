from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Home:
    URL = 'https://katalon-demo-cura.herokuapp.com/'
    BUTTON_MENU = (By.ID, 'menu-toggle')
    LOGIN_ITEM = (By.XPATH, '//*[@id="sidebar-wrapper"]/ul/li[3]/a')

    def __init__(self, driver: webdriver.Chrome):
        self.timeout = 5
        self.driver = driver

    def load(self):
        self.driver.get(url=self.URL)

    def open_menu(self):
        self.driver.find_element(*self.BUTTON_MENU).click()

    def open_login(self):
        login_element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.LOGIN_ITEM)
        )

        login_element.click()
