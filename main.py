"""
Encrypt number 5555555 and decrypt 5555555 using scheme
Prime number chosen between 5000 and 10000
List every intermediate step
"""


# CAN WE REALLY JUST
# CHOOSE ANY TWO PRIMES OR DOES IT NEED TO BE RANDOM
from functools import reduce


def euclidean_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return euclidean_gcd(a - b, b)

    return euclidean_gcd(a, b - a)


def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1

    gcdd, x1, y1 = extended_euclidean(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcdd, x, y


def solve_lin_cong(a, b, n):
    temp = extended_euclidean(n, a)
    y, d = temp[2], temp[0]
    m = n // d
    if b % d != 0:
        return False
    else:
        return y * b // d % m, m


def relative_prime(a, b):
    return euclidean_gcd(a, b) == 1


def modular_exponentiation(base, exponent, modulus):
    r = 1
    if r & exponent:
        r = base
    while exponent:
        exponent >>= 1
        base = (base * base) % modulus
        if exponent & 1:
            r = (r * base) % modulus
    return r


def encryption(p, q, m):
    if relative_prime(p, q - 1) and relative_prime(q, p - 1):
        print("coprime primes")
        pk_n = p * q  # public key
        print("public key ", pk_n)

        # solve congruence
        # answer in the form x mod y (e.g. 11, 17 means 11 mod 17)
        p_prime = solve_lin_cong(p, 1, (q - 1))
        q_prime = solve_lin_cong(q, 1, (p - 1))

        print("P : ", p_prime)
        print("Q : ", q_prime)

        # encrypted message
        c = modular_exponentiation(m, pk_n, pk_n)
        print("ENCRYPTED MESSAGE C = ", c)

        decryption(c, p, q, p_prime, q_prime)
    else:
        print("P and Q are not relatively prime")


def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc * b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def decryption(c, p, q, p_prime, q_prime):
    x1 = pow(c, p_prime[0] % p_prime[1])
    x2 = pow(c, q_prime[0] % p_prime[1])

    print(x1)
    print(x2)

    m = [q, p]
    a = [x1, x2]

    print("DECODED MESSAGE : ", chinese_remainder(m, a))


if __name__ == '__main__':
    P = int(input("Choose a prime number between 5000 and 10000 \n --> "))
    Q = int(input("Choose another prime number between 5000 and 10000 \n --> "))
    print("PLAIN TEXT : ", 3)
    encryption(P, Q, 3)