def is_palindrome_number(number):
    number = str(number)
    rev = number[::-1]
    return number == rev


def test_is_palindrome_number():
    assert is_palindrome_number(9)
    assert is_palindrome_number(99)
    assert is_palindrome_number(999)
    assert is_palindrome_number(9119)
    assert not is_palindrome_number(91)
    assert not is_palindrome_number(9118)


def get_largest_palindrome_product(factor_range):
    return max([x * y for x in factor_range for y in factor_range if is_palindrome_number(x * y)])


def test_get_largest_palindrome_product():
    assert get_largest_palindrome_product(range(10, 100)) == 9009


print(get_largest_palindrome_product(range(100, 1000)))
