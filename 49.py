1 '''
 2 The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
 3
 4 There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
 5
 6 What 12-digit number do you form by concatenating the three terms in this sequence?
 7
 8 '''
 9
10 import prime
11 from combinatorics import permutations
12
13 prime._refresh(10000)
14 for num in xrange(1000, 10000):
15     if str(num).find('0') >= 0: continue
16
17     if prime.isprime(num):
18         prime_permutations = { num: 1 }
19         for x in permutations(list(str(num))):
20             next_num = int(''.join(x))
21             if prime.isprime(next_num):
22                 prime_permutations[next_num] = 1
23
24         primes = sorted(prime_permutations.keys())
25         for a in xrange(0, len(primes)):
26             if primes[a] == 1487: continue
27             for b in xrange(a+1, len(primes)):
28                 c = (primes[a] + primes[b]) / 2
29                 if prime_permutations.has_key(c):
30                     print str(primes[a]) + str(c) + str(primes[b])
31                     exit()