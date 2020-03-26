def sum_square_difference(range):
    square_of_sum = sum(range)**2
    sum_of_squares = sum([x * x for x in range])
    return square_of_sum - sum_of_squares


def test_sum_square_difference():
    assert sum_square_difference(range(11)) == 2640


print(sum_square_difference(range(101)))