from GCD import cal_GCD

def test_GCD_of_two_numbers_are_equal_to_expected():
    test_cases = [
        [12, 8, 4],
        [15, 10, 5],
        [7, 3, 1],
        [100, 25, 25],
        [48, 18, 6],
        [5, 5, 5],
        [100, 100, 100],
        [1, 1, 1],
        [0, 5, 5],
        [5, 0, 5],
        [0, 0, 0],
        [-12, 8, 4],
        [12, -8, 4],
        [-12, -8, 4],
        [-7, 3, 1],
        [1, 100, 1],
        [100, 1, 1],
        [1000000, 500000, 500000],
        [1234567890, 10, 10],
        ["12", 8, False],
        [12, "8", False],
        ["abc", "xyz", False],
        [12.5, 5, False],
        [12, 5.5, False],
        [None, 5, False],
        [5, None, False],
        [True, 5, False],
        [5, False, False],
        [[], 5, False],
        [5, [], False],
        [{}, 5, False]
    ]

    for a, b, expected in test_cases:
        assert cal_GCD(a, b) == expected