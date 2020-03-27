import math


def triangle_number_generator():
    index = 0
    _sum = 0
    while True:
        index += 1
        _sum += index
        yield _sum


def test_triangle_number_generator():
    gen = triangle_number_generator()
    assert [next(gen) for x in range(10)] == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def get_factors(number):
    factors = []
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            factors.append(n)
            factors.append(number / n)
    factors.append(1)
    if (number != 1):
        factors.append(number)
    return factors


def test_get_factors():
    assert sorted(get_factors(1)) == [1]
    assert sorted(get_factors(3)) == [1, 3]
    assert sorted(get_factors(6)) == [1, 2, 3, 6]
    assert sorted(get_factors(10)) == [1, 2, 5, 10]
    assert sorted(get_factors(15)) == [1, 3, 5, 15]
    assert sorted(get_factors(21)) == [1, 3, 7, 21]
    assert sorted(get_factors(28)) == [1, 2, 4, 7, 14, 28]


def find_first_triangle_number_with_more_than_x_divisors(x):
    gen = triangle_number_generator()
    tri_num = next(gen)
    while len(get_factors(tri_num)) <= x:
        tri_num = next(gen)
    return tri_num


def test_find_first_triangle_number_with_more_than_x_divisors():
    assert find_first_triangle_number_with_more_than_x_divisors(5) == 28


print(find_first_triangle_number_with_more_than_x_divisors(500))
