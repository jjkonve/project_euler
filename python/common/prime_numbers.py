import math


def prime_number_generator():
    primes = [2]
    yield 2
    i = 3
    while(True):
        is_prime = True
        root = math.sqrt(i)
        for prime in primes:
            if prime > root:
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            yield i
        i += 2


def test_prime_number_generator():
    gen = prime_number_generator()
    assert [next(gen) for i in range(7)] == [2, 3, 5, 7, 11, 13, 17]
