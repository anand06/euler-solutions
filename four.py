'''
 2 A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
 3
 4 Find the largest palindrome made from the product of two 3-digit numbers.
 5 '''
 6
 7 n = 0
 8 for a in xrange(999, 100, -1):
 9     for b in xrange(a, 100, -1):
10         x = a * b
11         if x > n:
12             s = str(a * b)
13             if s == s[::-1]:
14                 n = a * b
15
16 print n