import pytest
import logging

from selenium import webdriver


@pytest.fixture()
def conf_func_fixture(request):
    """
    Auto function resource fixture
    """
    logging.info("start")
    def auto_func_teardown():
        logging.info("end")
        webdriver.Chrome().close()
    request.addfinalizer(auto_func_teardown)