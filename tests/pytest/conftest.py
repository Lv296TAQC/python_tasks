import pytest


@pytest.fixture(scope="session", autouse=False)
def conf_fixture(request):
    """
    Auto session resource fixture
    """
    print("Hello!")
    def auto_session_teardown():
        print("Bye!")
    request.addfinalizer(auto_session_teardown)


@pytest.fixture()
def conf_func_fixture(request):
    """
    Auto session resource fixture
    """
    print("start")
    def auto_func_teardown():
        print("end")
    request.addfinalizer(auto_func_teardown)