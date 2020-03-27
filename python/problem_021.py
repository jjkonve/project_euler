from common.sum_of_divisors import get_sum_of_divisors


def sum_of_amicable_numbers():
    sum_of_divisors = 0
    for i in range(1, 10000):
        _sum = get_sum_of_divisors(i)
        if _sum != i and get_sum_of_divisors(_sum) == i:
            sum_of_divisors += i
    return sum_of_divisors


print(sum_of_amicable_numbers())
