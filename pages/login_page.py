from base_page import BasePage
from selenium import webdriver
from page_objects import PageObject, PageElement
import pdb


class LoginPage(BasePage):

    # These are the class variables: they should be the same for any class
    # instance. I think.
    email = PageElement(id_='email')
    password = PageElement(id_='password')
    submit = PageElement(css='input[type="submit"]')
    error_on_submit = PageElement(css='h3.error')

    def __init__(self, driver):
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def fill_in_login_form(self, email, password):
        self.email = email
        self.password = password

    def submit_login_form(self):
        self.submit.click()
