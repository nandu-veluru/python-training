from TargetDate import days_to_reach_target
import random
import sys
import math
import unittest

a = random.randint(1, sys.maxsize)
b = random.randint(1, sys.maxsize)
c = math.ceil(a / b)

def test_target_amount_is_randomInteger_and_deposite_amount_is_randomInteger_required_to_reach_target_will_be():
    assert days_to_reach_target(a, b) == c 

def test_target_amount_is_0_and_deposite_amount_is_random_required_to_reach_Target_is_0_days():
    assert days_to_reach_target(0, b) == 0

class TestNone(unittest.TestCase):
    def test_the_number_is_None(number):
        msg = None
        number.assertIsNone(msg)

    

# def test_target_amount_is_30_and_deposite_amount_is_10_required_to_reach_Target_is_3_days():
#     assert days_to_reach_target(30, 10) == 3

# def test_target_amount_is_100_and_deposite_amount_is_10_required_to_reach_Target_is_10_days():
#     assert days_to_reach_target(100, 10) == 10

# def test_target_amount_is_50_and_deposite_amount_is_15_required_to_reach_Target_is_4_days():
#     assert days_to_reach_target(50, 15) == 4



# # def test_target_amount_is_100_and_deposite_amount_is_0_required_to_reach_Target_is_0_days():
# #     assert days_to_reach_target(0, 0) == "infinte days"

# def test_target_amount_is_10000_and_deposite_amount_is_77_required_to_reach_Target_is_130_days():
#     assert days_to_reach_target(10000, 77) == 130

# def test_target_amount_is_700000_and_deposite_amount_is_1357_required_to_reach_Target_is_516_days():
#     assert days_to_reach_target(700000, 1357) == 516

# def test_target_amount_is_1_and_deposite_amount_is_137_required_to_reach_Target_is_1_days():
#     assert days_to_reach_target(1, 137) == 1

# def test_target_amount_is_16735272_and_deposite_amount_is_1987_required_to_reach_Target_is_1_days():
#     assert days_to_reach_target(16735272, 1987) == 8423

# def test_target_amount_is_876_and_deposite_amount_is_1_required_to_reach_Target_is_876_days():
#     assert days_to_reach_target(876, 1) == 876






 






