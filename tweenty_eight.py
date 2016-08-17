 1 '''
 2 Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
 3  43                49
 4     21 22 23 24 25
 5     20  7  8  9 10
 6     19  6  1  2 11
 7     18  5  4  3 12
 8     17 16 15 14 13
 9  37                31
10                       57
11 1
12 6*4
13 19*4
14 39*4
15 69*4
16
17 It can be verified that the sum of both diagonals is 101.
18
19 What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?
20 '''
21
22 diagonal = 1
23 start = 1
24 for width in xrange(3, 1002, 2):
25     increment = width - 1
26     count = increment * 4
27     diagonal = diagonal + start * 4 + increment * 10
28     start = start + count
29
30 print diagonal