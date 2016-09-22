import pytest
from pages.login_page import LoginPage
from pytest_bdd import scenarios, scenario, given, when, then, parsers

scenarios('features')


@given("I am on the login page")
def author_user(driver):
    driver.get("http://millio-dashboard.relayr.io/login")
    global page
    page = LoginPage(driver)
    return page


@when(parsers.re("I login with (?P<email>.+) and (?P<pswd>.+)"))
def login_with_credentials(email, pswd):
    page.fill_in_login_form(email, pswd)
    page.submit_login_form()
    return page


@then('I see error message')
def verify_error_is_present():
    assert "doesn't exist." in page.error_on_submit.text
