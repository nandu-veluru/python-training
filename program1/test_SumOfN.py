from SumOfN import sumOfN 
import unittest
import random
import sys

a = random.randint(1, 99999)
ans = a * (a + 1) / 2


def test_sum_of_value_of_random_integer_is():
    assert sumOfN(a) == ans

def test_the_sum_of_0_number_is_0():
    assert sumOfN(0) == 0

class TestNone(unittest.TestCase):
    def test_the_number_is_None(number):
        msg = None
        number.assertIsNone(msg)

# def test_the_sum_of_4_numbers_is_10():
#     assert sumOfN(4) == 10

# def test_the_sum_of_1_number_is_1():
#     assert sumOfN(1) == 1

# def test_the_sum_of_2_numbers_is_3():
#     assert sumOfN(2) == 3



# def test_the_sum_of_50_numbers_is_1275():
#     assert sumOfN(50) == 1275

# def test_the_sum_of_100_numbers_is_5050():
#     assert sumOfN(100) == 5050

# def test_the_sum_of_200_numbers_is_20100():
#     assert sumOfN(200) == 20100

# def test_the_sum_of_negitive_Numbers_is_None():
#     assert sumOfN(-9) == None



    




