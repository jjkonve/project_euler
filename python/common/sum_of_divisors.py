import math


def get_sum_of_divisors(number):
    _sum = 1
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            _sum += n
            if n != number // n:
                _sum += number // n
    return _sum


def test_get_sum_of_divisors():
    assert get_sum_of_divisors(9) == 4
    assert get_sum_of_divisors(220) == 284
    assert get_sum_of_divisors(284) == 220
