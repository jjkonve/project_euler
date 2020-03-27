def collatz_sequence_length(start_number):
    length = 1
    i = start_number
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
        length += 1
    return length


def test_collatz_sequence_length():
    assert collatz_sequence_length(1) == 1
    assert collatz_sequence_length(13) == 10


def find_longest_collatz_sequence():
    longest_index, longest_length = 0, 0
    for i in range(1, 1000000):
        length = collatz_sequence_length(i)
        if length > longest_length:
            longest_index = i
            longest_length = length
    return longest_index


print(find_longest_collatz_sequence())
