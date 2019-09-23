# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(n):

    if n % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(n)), 2):
        if n % i == 0:
            return False

    return True

def largest_prime(n):

    # largest prime
    lpf = -1

    # n even
    if n % 2 == 0:
        lpf = 2


    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if is_prime(i) and n % i == 0:
            lpf = i

    return lpf

print(largest_prime(600851475143))

















