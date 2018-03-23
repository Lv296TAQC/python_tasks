import pytest
import allure

from tasks.task_87 import natural_number


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.mark.suit
@pytest.mark.parametrize('a, b, c', [
    (1234, 2, 7),
    (7200, 2, 0),
    (1510, 0, 0),
    (1, 4, 1),
    (815, 4, 14)
])
def test_natural_number_suitable_args(a, b, c):
    allure.environment(report='Allure report', browser='Ubuntu 16.04.3 LTS')
    allure.attach('my attach', 'Hello, World')
    with pytest.allure.step('step one'):
        with open('./15193170-stylized-vector-tree-Stock-Photo.jpg', 'rb') as img:
            f = img.read()
            pytest.allure.attach("screenshot", bytearray(f), type=allure.constants.AttachmentType.JPG)
    with pytest.allure.step('step two'):
        assert natural_number(a, b) == c


@pytest.mark.skip
@pytest.mark.exception
@pytest.mark.parametrize('a, b', [
    (-1234, 2),
    (557, -1),
    (5.57, 2),
    (3967, 8.9)
])
def test_natural_number_unsuitable_args(a, b):
    with pytest.raises(ValueError):
        natural_number(a, b)


@pytest.mark.exception
@pytest.mark.parametrize('a, b', [
    ('', 4),
    ('5dssa6578', 4),
    (8569, ''),
    (8569, '3'),
    ('d5fd5fd5', 't5')
])
def test_natural_number_str_args(a, b):
    with pytest.raises(TypeError):
        natural_number(a, b)
