import pytest
from tests.selenium_tests.conftest import driver


@pytest.mark.usefixtures("fixture_for_test")
def test_negative_login():
    driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()
    email = driver.find_element_by_id("input-email")
    email.send_keys("madborsuk@gmail.com")
    password = driver.find_element_by_id("input-password")
    password.send_keys("saxon123")
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
    #success = driver.find_element_by_xpath('//*[@id="account-login"]/div[1]').text
    #assert "No match for E-Mail Address and/or Password" in alert

    # need to complete
