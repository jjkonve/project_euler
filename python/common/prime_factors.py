from common.prime_numbers import prime_number_generator


def get_prime_factors(number):
    gen = prime_number_generator()
    prime = next(gen)
    while prime <= number:
        if number == prime:
            return [prime]
        if number % prime == 0:
            factors = get_prime_factors(number // prime)
            factors.append(prime)
            return factors
        prime = next(gen)
    return []


def test_get_prime_factors():
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(5) == [5]
    assert sorted(get_prime_factors(12)) == [2, 2, 3]
    assert sorted(get_prime_factors(13195)) == [5, 7, 13, 29]
