1 '''
 2 Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
 3
 4 1634 = 1^4 + 6^4 + 3^4 + 4^4
 5 8208 = 8^4 + 2^4 + 0^4 + 8^4
 6 9474 = 9^4 + 4^4 + 7^4 + 4^4
 7 As 1 = 1^4 is not a sum it is not included.
 8
 9 The sum of these numbers is 1634 + 8208 + 9474 = 19316.
10
11 Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
12 '''
13
14 def power_of_digits(n, p):
15     s = 0
16     while n > 0:
17         d = n % 10
18         n = n / 10
19         s = s + pow(d, p)
20     return s
21
22
23 print sum(n for n in xrange(2, 200000) if power_of_digits(n, 5) == n)