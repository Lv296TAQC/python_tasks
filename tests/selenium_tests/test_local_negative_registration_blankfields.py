import pytest
from tests.selenium_tests.conftest import driver


@pytest.mark.usefixtures("fixture_for_test")
def test_negative_login():

    driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[1]/a').click()
    driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()
    blankfirstname = driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div').text
    blanklastname = driver.find_element_by_xpath('//*[@id="account"]/div[3]/div/div').text
    blankemail = driver.find_element_by_xpath('//*[@id="account"]/div[4]/div/div').text
    blanktelephone = driver.find_element_by_xpath('//*[@id="account"]/div[5]/div/div').text
    blankpassword = driver.find_element_by_xpath('//*[@id="content"]/form/fieldset[2]/div[1]/div/div').text

    assert "First Name must be between 1 and 32 characters!" in blankfirstname
    assert "Last Name must be between 1 and 32 characters!" in blanklastname
    assert "E-Mail Address does not appear to be valid!" in blankemail
    assert "Telephone must be between 3 and 32 characters!" in blanktelephone
    assert "Password must be between 4 and 20 characters!" in blankpassword

