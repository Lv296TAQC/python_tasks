import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.selenium.user import user


def test_registration(conf_func_fixture):
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/opencart.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')))
    my_accont_tab = driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a')
    my_accont_tab.send_keys(Keys.RETURN)
    wait2 = WebDriverWait(driver, 10)
    wait2.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')))
    register = driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    register.send_keys(Keys.RETURN)
    driver.find_element_by_id("input-firstname").send_keys(user.first_name)
    driver.find_element_by_id("input-lastname").send_keys(user.last_name)
    driver.find_element_by_id("input-email").send_keys(user.email)
    driver.find_element_by_id("input-telephone").send_keys(user.tel)
    driver.find_element_by_id("input-password").send_keys(user.password)
    driver.find_element_by_id("input-confirm").send_keys(user.password)
    driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[1]').click()
    driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()
    assert driver.current_url == 'http://127.0.0.1/opencart.com/index.php?route=account/success'

