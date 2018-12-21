import math
import time


def primes_sieve(limit):
    """Generate primes"""
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            if i > limit:
                break
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


def get_divisor_sum(n):
    """Return divisor sum"""
    divisor_sum = 0
    max_root = math.sqrt(n)

    i = 1
    while i <= max_root:
        if n % i == 0:
            # If divisors are equal, take only one
            # of them
            if n / i == i:
                divisor_sum += i
            else:  # Otherwise take both
                divisor_sum += i
                divisor_sum += (n / i)
        i += 1

    # calculate sum of all proper divisors only
    divisor_sum -= n
    return divisor_sum


def is_abundant(n):
    return get_divisor_sum(n) > n


start = time.time()
sandwiched_rich_sum = 0
prev_prime = 1
for prime in primes_sieve(10**7):
    if prime - prev_prime == 2:
        possible_abundant = prime - 1
        if is_abundant(possible_abundant):
            sandwiched_rich_sum += possible_abundant
    prev_prime = prime

print(sandwiched_rich_sum)
end = time.time()
print(f'Runtime: {end - start:.4f} seconds')
