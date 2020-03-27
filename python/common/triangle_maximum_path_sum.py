def maximum_path_sum(triangle):
    previous_row = triangle[-1]
    for row in triangle[-2::-1]:
        new_row = []
        for i in range(len(row)):
            new_row.append(row[i] + max(previous_row[i], previous_row[i + 1]))
        previous_row = new_row
    return previous_row[0]


def test_maximum_path_sum():
    test_triangle = [
        [3, ],
        [7, 4, ],
        [2, 4, 6, ],
        [8, 5, 9, 3, ],
    ]

    assert maximum_path_sum(test_triangle) == 23
