1 '''
 2 The prime 41, can be written as the sum of six consecutive primes:
 3
 4 41 = 2 + 3 + 5 + 7 + 11 + 13
 5 This is the longest sum of consecutive primes that adds to a prime below one-hundred.
 6
 7 The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
 8
 9 Which prime, below one-million, can be written as the sum of the most consecutive primes?
10 '''
11 import prime
12
13 MAX = 5000
14 prime.prime(MAX)
15
16 def check_length(n, below):
17     maxprime = 0
18     for x in xrange(0, below):
19         total = sum(prime.prime_list[x:x+n])
20         if total > below: break
21         if prime.isprime(total): maxprime = total
22     return maxprime
23
24 for n in xrange(1000, 0, -1):
25     maxprime = check_length(n, 1000000)
26     if maxprime:
27         print maxprime