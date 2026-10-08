def sumOfN(n):
    if n < 0:
        return None
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
