1 '''
 2 A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
 3 a^2 + b^2 = c^2
 4 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 5
 6 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 7 Find the product abc.
 8 '''
 9
10 for a in xrange(1, 1000):
11     for b in xrange(a, 1000):
12         c = 1000 - a - b
13         if c > 0:
14             if c*c == a*a + b*b:
15                 print a*b*c
16                 break