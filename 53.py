1 '''
 2 There are exactly ten ways of selecting three from five, 12345:
 3
 4 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
 5
 6 In combinatorics, we use the notation, 5C3 = 10.
 7
 8 In general,
 9
10 nCr = n! / r!(nr)! where r <= n, n! = n x (n-1)...x 3 x 2 x 1, and 0! = 1.
11
12 It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
13
14 How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
15 '''
16
17 fact_c = { 0: 1, 1: 1 }
18 def fact(n): return fact_c.has_key(n) and fact_c[n] or fact_c.setdefault(n, n * fact(n-1))
19
20 count = 0
21 for n in xrange(1, 101):
22     for r in xrange(0, n):
23         ncr = fact(n) / fact(r) / fact(n-r)
24         if ncr > 1000000: count += 1
25 print count