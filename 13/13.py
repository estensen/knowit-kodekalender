def is_prime(n: int) -> bool:
    """Check if integer n is a prime"""
    if n < 2:
        return False
    # 2 is the only even prime number
    elif n == 2:
        return True
    # All other even numbers are not primes
    elif not n & 1:
        return False

    # Range starts with 3 and only needs to go up
    # The square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def get_christmas_sequence_prime_sum() -> int:
    """Return the sum of the first 100 primes from the Christmas sequence"""

    # Keep track of how many combinations that can create a number for each index number
    nums = [0] * 10**5 
    nums[1] = 1 
    nums[3] = 1 

    prime_sum = 0
    prime_count = 0
    
    i = 1 
    while prime_count < 100:
        # Is the number of distinct combination of prev seq?
        if nums[i] == 1:
            if is_prime(i):
                prime_sum += i
                prime_count += 1
            for j in range(i):
                if nums[j] == 1 and j != i:
                    nums[i+j] += 1
        i += 1
    return prime_sum    


print(get_christmas_sequence_prime_sum())

