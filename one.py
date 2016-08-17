 '''
 2 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 3
 4 Find the sum of all the multiples of 3 or 5 below 1000.
 5 '''
 6
 7 n = 0
 8 for i in xrange(1,1000):
 9     if not i % 5 or not i % 3:
10         n = n + i
11
12 print n