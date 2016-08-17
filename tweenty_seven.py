1 '''
 2 Euler published the remarkable quadratic formula:
 3
 4 n^2 + n + 41
 5
 6 It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
 7
 8 Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
 9
10 Considering quadratics of the form:
11
12 n^2 + an + b, where |a| <= 1000 and |b| <= 1000
13
14 where |n| is the modulus/absolute value of n
15 e.g. |11| = 11 and |4| = 4
16 Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
17
18 '''
19
20 import prime
21
22 max_pair = (0,0,0)
23 for a in xrange(-999, 1000):
24     for b in xrange(max(2, 1-a), 1000): # b >= 2, a + b + 1 >= 2
25         n, count = 0, 0
26         while True:
27             v = n*n + a*n + b
28             prime._refresh(v)
29             if prime.isprime(v): count = count + 1
30             else: break
31             n = n + 1
32         if count > max_pair[2]: