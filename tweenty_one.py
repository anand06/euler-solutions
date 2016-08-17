 1 '''
 2 Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 3 If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
 4
 5 For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
 6
 7 Evaluate the sum of all the amicable numbers under 10000.
 8 '''
 9
10 def divisors(n): return list(i for i in xrange(1, n/2+1) if n % i == 0)
11 pair = dict( ((n, sum(divisors(n))) for n in xrange(1, 10000)) )
12 print sum(n for n in xrange(1, 10000) if pair.get(pair[n], 0) == n and pair[n] != n)