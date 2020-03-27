def number_of_choices(size):
    choice_table = [[None] * (size + 1)] * (size + 1)
    choice_table[0][0] = 0
    for i in range(1, size + 1):
        choice_table[0][i] = 1
        choice_table[i][0] = 1
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            choice_table[y][x] = choice_table[y - 1][x] + choice_table[y][x - 1]
    return choice_table[size][size]


def test_number_of_choices():
    assert number_of_choices(2) == 6


print(number_of_choices(20))
