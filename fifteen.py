 1 '''
 2 Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
 3
 4 How many routes are there through a 20x20 grid?
 5 '''
 6
 7 def fact(n):
 8     f = 1
 9     for x in xrange(1, n+1): f = f * x
10     return f
11
12 print fact(40) / fact(20) / fact(20)