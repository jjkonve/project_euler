from common.fibonacci import fibonacci_generator


def index_of_first_fibonacci_to_contain_x_digits(x):
    gen = fibonacci_generator()
    i = 0
    while True:
        fib = next(gen)
        if len(str(fib)) == x:
            return i
        i += 1


def test_index_of_first_fibonacci_to_contain_x_digits():
    assert index_of_first_fibonacci_to_contain_x_digits(3) == 12


print(index_of_first_fibonacci_to_contain_x_digits(1000))
