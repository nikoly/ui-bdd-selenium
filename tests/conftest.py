from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import pdb


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Firefox()

    def close_driver():
        driver.quit()
    request.addfinalizer(close_driver)
    driver.set_window_size(800, 400)
    return driver
