1 '''
 2 Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
 3 '''
 4
 5 s = 0
 6 mod = pow(10, 10)
 7 for x in xrange(1, 1001):
 8     s = s + pow(x, x)
 9
10 print s % mod