import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.selenium.user import user


def test_login(conf_func_fixture):
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/opencart.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')))
    my_accont_tab = driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a')
    my_accont_tab.send_keys(Keys.RETURN)
    wait2 = WebDriverWait(driver, 10)
    wait2.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')))
    login = driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    login.send_keys(Keys.RETURN)
    driver.find_element_by_id("input-email").send_keys(user.email)
    driver.find_element_by_id("input-password").send_keys(user.password)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
    assert driver.current_url == 'http://127.0.0.1/opencart.com/index.php?route=account/account'