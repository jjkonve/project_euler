from common.prime_numbers import prime_number_generator


def get_nth_prime_number(n):
    gen = prime_number_generator()
    prime = 0
    for i in range(n):
        prime = next(gen)
    return prime


def test_get_nth_prime_number():
    assert get_nth_prime_number(6) == 13


print(get_nth_prime_number(10001))
