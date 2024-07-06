import pytest
from selenium import webdriver
from constants import Constants


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(Constants.URL)
    yield driver
    driver.quit()
