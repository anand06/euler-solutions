 1 '''
 2 The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
 3
 4 There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
 5
 6 How many circular primes are there below one million?
 7 '''
 8
 9 sieve = [True] * 1000000
10 sieve[0] = sieve[1] = False
11
12 def mark(sieve, x):
13     for i in xrange(x+x, len(sieve), x):
14         sieve[i] = False
15
16 for x in xrange(2, int(len(sieve) ** 0.5) + 1):
17     mark(sieve, x)
18
19 def circular(n):
20     digits = []
21     while n > 0:
22         digits.insert(0, str(n % 10))
23         n = n / 10
24     for d in xrange(1, len(digits)):
25         yield int(''.join(digits[d:] + digits[0:d]))
26
27 count = 0
28 for n, p in enumerate(sieve):
29     if p:
30         iscircularprime = 1
31         for m in circular(n):
32             if not sieve[m]:
33                 iscircularprime = 0
34                 break
35         if iscircularprime:
36             count = count + 1
37
38 print count