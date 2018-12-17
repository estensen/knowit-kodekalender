import requests
import time
from typing import List


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


def get_biggest_palindrome(nums: List[int], ix: int) -> int:
    biggest_palindrome = 0
    palindrome_sum = nums[ix]

    for i in range(1, len(nums) // 2):
        if i > ix:
            break
        elif ix + i > len(nums) - 1:
            break
        elif nums[ix-i] != nums[ix+i]:
            break
        
        palindrome_sum += nums[ix-i] + nums[ix+i]
        if is_prime(palindrome_sum):
            biggest_palindrome = palindrome_sum 

    return biggest_palindrome


url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-palindrom.txt'
r = requests.get(url)
data = r.text.split(',')
nums = list(map(int, data))

start = time.time()
biggest_prime_palindrome_sum = 0
for i in range(len(nums)):
    biggest_prime_palindrome_sum = max(biggest_prime_palindrome_sum, get_biggest_palindrome(nums, i))

print(biggest_prime_palindrome_sum)
end = time.time()
print(f'Runtime: {round(end - start)} seconds')

