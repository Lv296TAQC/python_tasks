import pytest
from selenium import webdriver


def setUp(self):
    self.driver = webdriver.Chrome("chromedriver.exe")


def test_negative_login():
    driver = webdriver.Chrome("F:\\install\\Selenium\\chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.get("http://127.0.0.1:1234/opencart.com/")
    driver.implicitly_wait(100)
#    driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/span").click()  # Don't need this because of href
#    driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
    driver.get("http://localhost:1234/opencart.com/index.php?route=account/login")  # Instead of 14 and 15 lines
    email = driver.find_element_by_id("input-email")
    email.send_keys("wrongemail")
    password = driver.find_element_by_id("input-password")
    password.send_keys("wrongpassword")
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
    alert = driver.find_element_by_xpath('//*[@id="account-login"]/div[1]').text
    assert "Your account has exceeded allowed number of login attempts. Please try again in 1 hour" in alert


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    pytest.main()
