def is_multiple_of_three_or_five(number):
    return number % 3 == 0 or number % 5 == 0


def test_is_multiple_of_three_or_five():
    assert is_multiple_of_three_or_five(3)
    assert is_multiple_of_three_or_five(6)
    assert is_multiple_of_three_or_five(5)
    assert is_multiple_of_three_or_five(15)
    assert not is_multiple_of_three_or_five(4)


def solution(max_natural_number):
    return sum([i for i in range(1, max_natural_number) if is_multiple_of_three_or_five(i)])


def test_solution():
    assert solution(10)


print(solution(1000))
