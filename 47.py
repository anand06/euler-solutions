 1 '''
 2 Find the first four consecutive integers to have four distinct prime factors
 3 '''
 4
 5 import prime
 6
 7 def distinct_factors(n): return len(dict.fromkeys(prime.factors(n)).keys())
 8
 9 factors = [0, 1, distinct_factors(2), distinct_factors(3)]
10 while True:
11     if factors[-4::] == [4,4,4,4]: break
12     else: factors.append(distinct_factors(len(factors)))
13
14 print len(factors)-4