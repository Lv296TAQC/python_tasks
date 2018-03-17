import pytest
import logging
from logging.config import fileConfig
from tasks.task_178b import count_sq


fileConfig('logging_config.ini')
logger = logging.getLogger(__name__)

logger.info('Start reading database')


def test_01_task_178b():
    assert count_sq((1, 2, 3, 5, 6, 36, 4, 16)) == 3


def test_02_task_178b():
    with pytest.raises(TypeError):
        count_sq('abc')


def test_03_task_178b():
    with pytest.raises(TypeError):
        count_sq({'346'})


def test_04_task_178b():
    with pytest.raises(TypeError):
        count_sq(8)


def test_05_task_178b():
    with pytest.raises(TypeError):
        count_sq()


logger.info('Finish updating records')
