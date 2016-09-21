import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.login_page import LoginPage
import pdb


class TestLogin:

    def test_login_user(self, driver):

        driver.get("http://millio-dashboard.relayr.io/login")
        email = "dummy@relayr.de"
        password = "dummy"

        page = LoginPage(driver)
        page.fill_in_login_form(email, password)
        page.submit_login_form()

        assert "User {} doesn't exist.".format(email) in page.error_on_submit.text
