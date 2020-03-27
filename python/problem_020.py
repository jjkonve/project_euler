def factorial_digit_sum(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return sum([int(x) for x in str(factorial)])


def test_factorial_digit_sum():
    factorial_digit_sum(10) == 27


print(factorial_digit_sum(100))
