import pytest
from tasks.task_559 import is_prime_number, return_prime_number, number_of_mercenn


@pytest.mark.suit
def test_is_5_prime_number():
    assert is_prime_number(5)


@pytest.mark.skipif(True, reason='some reason')
@pytest.mark.suit
def test_is_10_not_prime_number():
    assert not is_prime_number(10)


@pytest.mark.exception
@pytest.mark.parametrize('a', [-7, 0, 2.0])
def test_is_prime_number_unsuitable_arg(a):
    with pytest.raises(ValueError):
        is_prime_number(a)


@pytest.mark.exception
@pytest.mark.parametrize('a', ['25', 'hhg', ''])
def test_is_prime_number_str_arg(a):
    with pytest.raises(TypeError):
        is_prime_number(a)


@pytest.mark.suit
def test_return_prime_number_suitable_arg():
    assert return_prime_number(6) == [1, 2, 3, 5]


@pytest.mark.exception
@pytest.mark.parametrize('a', [-12, 1.0])
def test_return_prime_number_unsuitable_arg(a):
    with pytest.raises(ValueError):
        return_prime_number(a)


@pytest.mark.exception
@pytest.mark.parametrize('a', ['6', '2#6'])
def test_return_prime_number_str_arg(a):
    with pytest.raises(TypeError):
        return_prime_number(a)


@pytest.mark.suit
def test_number_of_mercenn_suitable_arg():
    assert return_prime_number(10) == [3, 7]


@pytest.mark.exception
@pytest.mark.parametrize('a', [-142, 10.5])
def test_number_of_mercenn_unsuitable_arg(a):
    with pytest.raises(ValueError):
        return_prime_number(a)


@pytest.mark.exception
@pytest.mark.parametrize('a', ['788', 'sd8'])
def test_number_of_mercenn_str_arg(a):
    with pytest.raises(TypeError):
        return_prime_number(a)
