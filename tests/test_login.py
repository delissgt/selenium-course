from selenium import webdriver

from page_objects.home import Home
from page_objects.login import Login


def test_login():
    driver = webdriver.Chrome()

    home_page = Home(driver)
    login_page = Login(driver)

    home_page.load()

    home_page.open_menu()
    home_page.open_login()

    assert login_page.get_username_value() == 'John Doe'

    assert login_page.get_password_value() == 'ThisIsNotAPassword'

    login_page.set_username_login_value()
    login_page.set_password_login_value()
    login_page.button_login_click()

    assert driver.current_url == 'https://katalon-demo-cura.herokuapp.com/#appointment'
