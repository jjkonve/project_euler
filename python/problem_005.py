from common.prime_factors import get_prime_factors


class CommonOccurrenceDict():
    def __init__(self):
        self.dict = {}

    def add_items(self, _list):
        temp_dict = {}
        for item in _list:
            if not item in temp_dict:
                temp_dict[item] = 0
            temp_dict[item] += 1
        for key in temp_dict:
            if not key in self.dict:
                self.dict[key] = 0
            self.dict[key] = max(self.dict[key], temp_dict[key])

    def to_list(self):
        _list = []
        for key, value in self.dict.items():
            for i in range(value):
                _list.append(key)
        return _list


class TestCommonOccurrenceDict():
    def test_add_items(self):
        _dict = CommonOccurrenceDict()
        _dict.add_items([1, 2, 1, 1, 3])
        assert _dict.dict == {1: 3, 2: 1, 3: 1}
        _dict.add_items([1, 1, 2, 2, 4])
        assert _dict.dict == {1: 3, 2: 2, 3: 1, 4: 1}

    def test_to_list(self):
        _dict = CommonOccurrenceDict()
        _dict.dict = {1: 2, 2: 1, 3: 2}
        assert _dict.to_list() == [1, 1, 2, 3, 3]


def get_smallest_multiple(divisible_factors):
    _dict = CommonOccurrenceDict()
    for factor in divisible_factors:
        _dict.add_items(get_prime_factors(factor))
    product = 1
    for factor in _dict.to_list():
        product *= factor
    return product


def test_get_smallest_multiple():
    assert get_smallest_multiple(range(2, 11)) == 2520


print(get_smallest_multiple(range(2, 21)))
