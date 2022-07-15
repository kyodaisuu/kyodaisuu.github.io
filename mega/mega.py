#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Calculate last digit of mega
# See https://kyodaisuu.github.io/mega/
# Author: Fish
# MIT License

def main():
    """Calculate last digits of mega"""
    import sys
    import time
    # Set high recursion limit, the maximum depth of the Python stack.
    # as this program uses high recursion.
    sys.setrecursionlimit(10000)
    # Test that this program is working properly
    test()
    # Calculate last digits of Mega and save to a text file
    for d in (10, 100, 1000, 10000):  # for these digits
        time_sta = time.time()
        m = mega(d)
        time_end = time.time()
        tim = time_end - time_sta
        filename = 'mega' + str(d) + '.txt'
        with open(filename, mode='w') as f:
            f.write(str(m))
        print('Last {0} digits of Mega calculated in {1:.3}s and written to {2}.'.format(
            d, tim, filename))


def test():
    """Test calculation"""
    assert pow2mod(23, 1) == 8
    assert pow2mod(1003, 3) == 8
    assert pow2mod(234000, 7) == 1749376
    for d in range(17):
        assert mega(d) == 1993539660742656 % (10**d)


def powmod(a, b, r):
    """(a^b) mod r"""
    if b <= 2:
        return (a**b) % r
    if b <= 2**100:
        c = 2
    # For minimising recursion
    elif b <= 2**10000:
        c = 2**100
    else:
        c = 2**10000
    q, m = divmod(b, c)  # b = qc + m
    # Calculate a^b = (a^c)^q * a^m with mod r
    result = powmod(powmod(a, c, r), q, r) * powmod(a, m, r)
    return result % r


def pow2mod(n, d):
    """Last d digits of 2^n. Namely 2^n mod (10^d)"""
    if d == 1:
        if n == 0:
            return 1
        # When d=1 and n>0, as 2^n % 10 = permutation of {2, 4, 8, 6},
        # 2^n = 2^((n-1) % 4 + 1) (mod 10).
        return 2**((n-1) % 4 + 1) % 10
    # Now for d > 1.
    # From Euler's theeorem, 2^φ(5^d) = 1 (mod 5^d)
    # where φ(5^d) = (5^d)(1-1/5) = 4*5^(d-1)
    # and as 10^d is divisible by φ(5^d) when d>1
    # 2^(10^d) = 1 (mod 5^d) for d>1
    # Therefore 2^(10^d + d) = 2^d (mod 10^d)
    # 2^n can be recursively calculated as 2^n = 2^((n-d) % 10^d + d) (mod 10^d) for n>d
    r = 10**d
    if n > d:
        n = (n - d) % r + d
    # Now we calculate (2^n) mod (10^d)
    # We use powmod function for efficient calculation.
    return powmod(2, n, r)


def pow256mod(n, d):
    """Last d digits of 256^n"""
    # 256^n = 2^(8 * n)
    return pow2mod(8*n, d)


def mn(n, d):
    """Last d digits of m(n)

    where m(n) =
      (1) 0 when n = 0
      (2) 256^(m(n-1)) + m(n-1) otherwise
    """
    if n == 0:
        return 0
    m = mn(n-1, d)
    m = pow256mod(m, d) + m
    return m % (10**d)


def mega(d):
    """Last d digits of Mega"""
    d = int(d)
    if d < 1:
        return 0
    m = mn(256, d)
    m = pow256mod(m, d)
    m = pow256mod(m, d)
    return m


if __name__ == '__main__':
    main()
