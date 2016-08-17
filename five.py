 1 '''
 2 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 3
 4 What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
 5 '''
 6
 7 def gcd(a,b): return b and gcd(b, a % b) or a
 8 def lcm(a,b): return a * b / gcd(a,b)
 9
10 n = 1
11 for i in xrange(1, 21):
12     n = lcm(n, i)
13
14 print n