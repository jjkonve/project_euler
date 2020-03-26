def product_of_first_pythagorian_triplet_with_sum(_sum):
    for c in range(1, _sum):
        for b in range((_sum - c) // 2, min(c, _sum - c)):
            a = _sum - c - b
            if a**2 + b**2 == c**2:
                return a * b * c


def test_product_of_first_pythagorian_triplet_with_sum():
    assert product_of_first_pythagorian_triplet_with_sum(12) == 60


print(product_of_first_pythagorian_triplet_with_sum(1000))
