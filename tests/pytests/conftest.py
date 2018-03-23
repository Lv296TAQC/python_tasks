import pytest


@pytest.fixture(scope='session', autouse=False)
def mock_divisor_value(request):
    pytest_plugins = 'allure.pytest_plugin'
    message = "Fixture start work"

    def fin():
        print("Teardown by finalizer")
    request.addfinalizer(fin)

    return message
