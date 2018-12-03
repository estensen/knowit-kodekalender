magic_number = 4_294_967_296
num_prime_factors = 24
max_possible_prime_candidate = int(magic_number / (2**(num_prime_factors-1)))


def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            if i > max_possible_prime_candidate:
                break
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


def find_christmas_numbers(partial_product, product_index, prime_index=0):
    count = 0

    # Base case recursion: multiply product with 1
    if product_index == 13:
        return 1

    for i, prime in enumerate(primes[prime_index:]):
        product = partial_product * prime
        if product < magic_number:
            count += find_christmas_numbers(product, product_index+1, prime_index+i)
        else:
            break

    return count


"""
Doing some hand calculations I discovered that 2**11 * 3**13 is just under the max value,
which means that there will for all combinations be 11 2s.
We only need to check for combinations for the 13 first numbers.
"""
num_of_2s = 11

primes = list(primes_sieve(max_possible_prime_candidate))
print(find_christmas_numbers(2**num_of_2s, 0))
