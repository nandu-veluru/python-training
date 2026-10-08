import math
import sys
import random

def sumOfN(n):
    if n < 0:
        return None
    
    total = 0
    for i in range(1, n):
        total += i
    return total

n = random.randint(1, sys.maxsize)
result = sumOfN(n)
print(result)
