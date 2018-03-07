import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/")

    def teardown():
        driver.quit()
