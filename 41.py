1 '''
 2 We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
 3
 4 What is the largest n-digit pandigital prime that exists?
 5 '''
 6
 7 import prime
 8 from combinatorics import permutations
 9
10 # Pan-digital primes are 4 or 7 digits. Others divisible by 3
11 prime._refresh(2766)    # sqrt(7654321)
12 for perm in permutations(range(7, 0, -1)):
13     num = 0
14     for n in perm: num = num * 10 + n
15     if prime._isprime(num):
16         print num
17         break