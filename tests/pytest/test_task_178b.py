import pytest
import logging

from tasks.task_178_b import multiple_numbers

logging.basicConfig(level=logging.DEBUG,
                    format='# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename="my_log.log",
                    filemode="w")


@pytest.mark.suit
@pytest.mark.parametrize('a, b', [
    ([6, 21, 96, 110], 3),
    ([-110, 5, 78], 0),
    ([1, 8, 6, 1, 5, 78], 1)
])
def test_multiple_numbers_suitable_args(a, b):
    temp = multiple_numbers(a)
    logging.debug('multiple_numbers({}) => {}, expected: {}'.format(a, temp, b))
    assert temp == b


@pytest.mark.skipif(True, reason='some reason')
@pytest.mark.exception
@pytest.mark.parametrize('a', ['', '58, -64, 9, 11'])
def test_multiple_numbers_str_arg(a):
    with pytest.raises(TypeError):
        multiple_numbers(a)
