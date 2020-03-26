import math

def fibonacci_generator(max_number=math.inf):
    a = 0
    b = 1
    while (a <= max_number):
        yield a
        temp = a + b
        a = b
        b = temp
    return


def test_fibonacci_generator_without_parameter():
    gen = fibonacci_generator()
    fib = []
    for n in range(10):
        fib.append(next(gen))
    assert fib == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_generator_with_parameter():
    assert [n for n in fibonacci_generator(40)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


print(sum([n for n in fibonacci_generator(4000000) if n % 2 == 0]))
