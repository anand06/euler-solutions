 1 '''
 2 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
 3
 4 Find the sum of all numbers which are equal to the sum of the factorial of their digits.
 5
 6 Note: as 1! = 1 and 2! = 2 are not sums they are not included.
 7 '''
 8
 9 fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
10
11 def sum_of_digits_factorial(n):
12     s = 0
13     while n > 0:
14         d = n % 10
15         s = s + fact[d]
16         n = n / 10
17     return s
18
19 print sum(n for n in xrange(10, 100000) if n == sum_of_digits_factorial(n))