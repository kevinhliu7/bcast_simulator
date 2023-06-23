def power_of_two(n: int):
    if (n & (n-1) == 0) and n != 0:
        return 1
    return 0
