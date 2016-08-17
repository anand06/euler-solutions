 1 '''
 2 A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
 3
 4 A number whose proper divisors are less than the number is called deficient and a number whose proper divisors exceed the number is called abundant.
 5
 6 As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
 7
 8 Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
 9 '''
10
11 import prime
12
13 MAX = 28124
14 prime._refresh(MAX/2)
15 abundants = [n for n in xrange(1, MAX) if sum(prime.all_factors(n)) > n+n]
16 abundants_dict = dict.fromkeys(abundants, 1)
17
18 total = 0
19 for n in xrange(1, MAX):
20     sum_of_abundants = 0
21     for a in abundants:
22         if a > n: break
23         if abundants_dict.get(n - a):
24             sum_of_abundants = 1
25             break
26     if not sum_of_abundants:
27         total = total + n
28
29 print total