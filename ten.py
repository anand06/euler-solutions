 1 '''
 2 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 3
 4 Find the sum of all the primes below two million.
 5 '''
 6
 7 sieve = [True] * 2000000    # Sieve is faster for 2M primes
 8
 9 def mark(sieve, x):
10     for i in xrange(x+x, len(sieve), x):
11         sieve[i] = False
12
13 for x in xrange(2, int(len(sieve) ** 0.5) + 1):
14     if sieve[x]: mark(sieve, x)
15
16 print sum(i for i in xrange(2, len(sieve)) if sieve[i])