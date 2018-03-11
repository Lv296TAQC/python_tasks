import pytest
#  from unittest.mock import patch
#  from tasks.task_227 import divisor


@pytest.fixture(scope='session', autouse=False)
def mock_divisor_value(request):
    message = "Fixture start work"

    def fin():
        print("Teardown by finalizer")
    request.addfinalizer(fin)

    # with patch("tasks.task_227.divisor") as divisor_:
    #     divisor_.divisor.return_value = [1, 2, 3, 6]
    #
    #  def divisor_teardown():
    #      print('Allah akbar')
    #  divisor_.addfinalizer(divisor_teardown)

    return message
