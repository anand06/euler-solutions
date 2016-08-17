 1 '''
 2 The following iterative sequence is defined for the set of positive integers
 3 n -> n/2 (n is even)
 4 n -> 3n + 1 (n is odd)
 5
 6 Using the rule above and starting with 13, we generate the following sequence:
 7 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
 8
 9 It can be seen that this sequence (starting at 13 and fiinishing at 1) contains 10 terms.
10 Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
11
12 Which starting number, under one million, produces the longest chain?
13
14 NOTE: Once the chain starts the terms are allowed to go above one million.
15 '''
16
17 cache = { 1: 1 }
18 def chain(cache, n):
19     if not cache.get(n,0):
20         if n % 2: cache[n] = 1 + chain(cache, 3*n + 1)
21         else: cache[n] = 1 + chain(cache, n/2)
22     return cache[n]
23
24 m,n = 0,0
25 for i in xrange(1, 1000000):
26     c = chain(cache, i)
27     if c > m: m,n = c,i
28
29 print n