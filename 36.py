1 '''
 2 The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
 3
 4 Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
 5
 6 (Please note that the palindromic number, in either base, may not include leading zeros.)
 7 '''
 8
 9 def ispalindrome(n, base):
10     digits = []
11     reverse = []
12     while n > 0:
13         d = str(n % base)
14         digits.append(d)
15         reverse.insert(0, d)
16         n = n / base
17     return digits == reverse
18
19 print sum(n for n in xrange(1, 1000000) if ispalindrome(n, 10) and ispalindrome(n, 2))