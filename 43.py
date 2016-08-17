1 '''
 2 The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
 3
 4 Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
 5
 6 d2 d3 d4 = 406 is divisible by 2
 7 d3 d4 d5 = 063 is divisible by 3
 8 d4 d5 d6 = 635 is divisible by 5
 9 d5 d6 d7 = 357 is divisible by 7
10 d6 d7 d8 = 572 is divisible by 11
11 d7 d8 d9 = 728 is divisible by 13
12 d8 d9 d10= 289 is divisible by 17
13
14 Find the sum of all 0 to 9 pandigital numbers with this property.
15 '''
16
17 from combinatorics import permutations
18
19 def num(l):
20     s = 0
21     for n in l: s = s * 10 + n
22     return s
23
24 def subdiv(l, n): return num(l) % n == 0
25
26 total = 0
27 for perm in permutations((0,1,2,3,4,6,7,8,9)):
28     perm.insert(5, 5)               # d6 must be 5
29     if (subdiv(perm[7:10], 17) and
30         subdiv(perm[6:9],  13) and
31         subdiv(perm[5:8],  11) and
32         subdiv(perm[4:7],   7) and
33         subdiv(perm[3:6],   5) and
34         subdiv(perm[2:5],   3) and
35         subdiv(perm[1:4],   2)):
36             total += num(perm)
37
38 print total