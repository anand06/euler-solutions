1 '''
 2 It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
 3
 4  9 =  7 + 2 x 1^2
 5 15 =  7 + 2 x 2^2
 6 21 =  3 + 2 x 3^2
 7 25 =  7 + 2 x 3^2
 8 27 = 19 + 2 x 2^2
 9 33 = 31 + 2 x 1^2
10 It turns out that the conjecture was false.
11
12 What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
13 '''
14
15 import prime
16 MAX = 10000
17 squares = dict.fromkeys((x*x for x in xrange(1, MAX)), 1)
18 prime._refresh(MAX)
19
20 for x in xrange(35, MAX, 2):
21     if not prime.isprime(x):
22         is_goldbach = 0
23         for p in prime.prime_list[1:]:
24             if p >= x: break
25             if squares.has_key((x - p)/2):
26                 is_goldbach = 1
27                 break
28         if not is_goldbach:
29             print x
30             break