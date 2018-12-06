def zero_heavy(num: int) -> bool:
    num_str = str(num)
    zeros = sum([1 if c == '0' else 0 for c in num_str])
    return zeros > len(num_str) // 2

MAGIC_NUMBER = 18_163_106
print(sum([num if zero_heavy(num) else 0 for num in range(1, MAGIC_NUMBER)]))

