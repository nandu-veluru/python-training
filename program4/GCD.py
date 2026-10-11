def cal_GCD(a, b):
    if not isinstance(a, int) or isinstance(a, bool):
        return False
    if not isinstance(b, int) or isinstance(b, bool):
        return False
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a