def power_digit_sum(exponent):
    number = 2 ** exponent
    return sum([int(x) for x in str(number)])


def test_power_digit_sum():
    assert power_digit_sum(15) == 26


print(power_digit_sum(1000))
