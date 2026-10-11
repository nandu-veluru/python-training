from reverseNumber import integer_reverse

def test_reverse_of_numbers_maches_with_expected():
    inputs = [
        1234,
        10,
        0,
        -98,
        7,
        "hello",
        "123",
        12.5,
        None,
        True,
        False
    ]

    expected = [
        4321,
        1,
        0,
        -89,
        7,
        False,
        False,
        False,
        False,
        False,
        False
    ]

    for i in range(len(inputs)):
        assert integer_reverse(inputs[i]) == expected[i]