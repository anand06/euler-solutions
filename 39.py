1 '''
 2 If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
 3
 4 {20,48,52}, {24,45,51}, {30,40,50}
 5
 6 For which value of p < 1000, is the number of solutions maximised?
 7 '''
 8
 9 maxp, maxsol = 0, 0
10 for p in xrange(12, 1001, 2):
11     solutions = 0
12     # a < b < c. So a is at most 1/3 of p. b is between a and (p-a)/2
13     for a in xrange(1, p/3):
14         a2 = a*a
15         for b in xrange(a, (p-a)/2):
16             c = p - a - b
17             if a2 + b*b == c*c: solutions = solutions + 1
18     if solutions > maxsol: maxp, maxsol = p, solutions
19
20 print maxp