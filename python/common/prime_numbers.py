def prime_number_generator():
    primes = []
    i = 2
    while(True):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
            yield i
        i += 1


def test_prime_number_generator():
    gen = prime_number_generator()
    assert [next(gen) for i in range(5)] == [2, 3, 5, 7, 11]
