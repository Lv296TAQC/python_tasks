import pytest
import logging


@pytest.fixture(scope="session", autouse=False)
def conf_fixture(request):
    """
    Auto session resource fixture
    """
    logging.info("Hello!")
    def auto_session_teardown():
        logging.info("Bye!")
    request.addfinalizer(auto_session_teardown)


@pytest.fixture()
def conf_func_fixture(request):
    """
    Auto function resource fixture
    """
    logging.info("start")
    def auto_func_teardown():
        logging.info("end")
    request.addfinalizer(auto_func_teardown)