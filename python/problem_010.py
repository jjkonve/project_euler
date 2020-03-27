from common.prime_numbers import prime_number_generator


def sum_of_primes_below_x(x):
    _sum = 0
    gen = prime_number_generator()
    prime = next(gen)
    while prime < x:
        _sum += prime
        prime = next(gen)
    return _sum


def test_sum_of_primes_below_x():
    assert sum_of_primes_below_x(10) == 17


print(sum_of_primes_below_x(2000000))
