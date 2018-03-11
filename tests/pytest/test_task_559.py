import pytest
from tasks.task_559 import is_prime_number, return_prime_number, number_of_mercenn


def test_is_5_prime_number():
    assert is_prime_number(5)


def test_is_10_not_prime_number():
    assert not is_prime_number(10)


def test_is_prime_number_negative_arg():
    with pytest.raises(ValueError):
        is_prime_number(-7)


@pytest.mark.parametrize('a', [
    ('25'),
    ('hhg')
])
def test_is_prime_number_str_arg(a):
    with pytest.raises(TypeError):
        is_prime_number(a)


def test_return_prime_number_normal_arg():
    assert return_prime_number(6) == [1, 2, 3, 5]


def test_return_prime_number_negative_arg():
    with pytest.raises(ValueError):
        return_prime_number(-12)


@pytest.mark.parametrize('a', [
    ('6'),
    ('2#6')
])
def test_return_prime_number_str_arg(a):
    with pytest.raises(TypeError):
        return_prime_number(a)


def test_number_of_mercenn_normal_arg():
    assert return_prime_number(10) == [3, 7]


def test_number_of_mercenn_negative_arg():
    with pytest.raises(ValueError):
        return_prime_number(-142)


@pytest.mark.parametrize('a', [
    ('788'),
    ('sd8')
])
def test_number_of_mercenn_str_arg(a):
    with pytest.raises(TypeError):
        return_prime_number(a)
