import pytest
from tasks.task_569 import is_prime, prime_numbers, divide_by_prime, validate, natural_numbers


def test_is_prime():
    assert is_prime(7) == True


def test_is_prime_raises():
    with pytest.raises(TypeError):
        is_prime('wqwe')


@pytest.mark.parametrize('a, b', [
    (32, [7, 11, 13, 17, 19, 23, 29, 31]),
    (9, [7])
])
def test_prime_numbers(a, b):
    assert prime_numbers(a) == b


@pytest.mark.parametrize('a', [
    ('123'),
    ([123, 32])
])
def test_prime_numbers_raises(a):
    assert prime_numbers(a)


def test_prime_numbers_raise():
    with pytest.raises(TypeError):
        prime_numbers([12])


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_divide_by_prime():
    assert divide_by_prime(7) == False


def test_divide_by_prime_raise():
    with pytest.raises(TypeError):
        divide_by_prime()


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_validate():
    assert validate(100) == False


def test_validate_raise():
    with pytest.raises(TypeError):
        validate({2: '12'})


def test_natural_numbers():
    assert natural_numbers(9) == [30, 60, 90, 120, 150, 180, 240, 270, 300]
