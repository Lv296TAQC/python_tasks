import pytest
from selenium import webdriver


def setUp(self):
    self.driver = webdriver.Chrome("chromedriver.exe")


def test_negative_login():
    driver = webdriver.Chrome("F:\\install\\Selenium\\chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.get("http://127.0.0.1:1234/opencart.com/")
    driver.get("http://localhost:1234/opencart.com/index.php?route=account/register")
    driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()
    blankfirstname = driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div').text
    assert "First Name must be between 1 and 32 characters!" in blankfirstname


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    pytest.main()
