import pytest
from tests.selenium_tests.conftest import driver


@pytest.mark.usefixtures("fixture_for_test")
def test_negative_login():
    driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()
#    driver.get("http://localhost:1234/opencart.com/index.php?route=account/login")  # Instead of 14 and 15 lines
    email = driver.find_element_by_id("input-email")
    email.send_keys("wrongemail")
    password = driver.find_element_by_id("input-password")
    password.send_keys("wrongpassword")
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
    alert = driver.find_element_by_xpath('//*[@id="account-login"]/div[1]').text
    assert "Your account has exceeded allowed number of login attempts. Please try again in 1 hour" in alert
