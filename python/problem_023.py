from common.sum_of_divisors import get_sum_of_divisors


def find_abundant_numbers():
    numbers = set()
    for n in range(1, 28123):
        if get_sum_of_divisors(n) > n:
            numbers.add(n)
    return numbers


def sum_of_non_abundant_sums():
    _sum = 0
    abundant_numbers = find_abundant_numbers()
    for n in range(1, 28123):
        is_candidate = True
        for i in abundant_numbers:
            if (n - i) in abundant_numbers:
                is_candidate = False
                break
        if is_candidate:
            _sum += n
    return _sum


print(sum_of_non_abundant_sums())
