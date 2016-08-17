1 '''
 2 Find the sum of digits in 100!
 3 '''
 4
 5 def digits(n):
 6     s = 0
 7     while n > 0:
 8         s = s + (n % 10)
 9         n = n / 10
10     return s
11
12 n = 1
13 for i in xrange(1,100): n = n*i
14 print digits(n)