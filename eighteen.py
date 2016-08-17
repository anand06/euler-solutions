1 '''
 2 By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
 3
 4 3
 5 7 5
 6 2 4 6
 7 8 5 9 3
 8
 9 That is, 3 + 7 + 4 + 9 = 23.
10
11 Find the maximum total from top to bottom of the triangle below:
12
13 75
14 95 64
15 17 47 82
16 18 35 87 10
17 20 04 82 47 65
18 19 01 23 75 03 34
19 88 02 77 73 07 63 67
20 99 65 04 28 06 16 70 92
21 41 41 26 56 83 40 80 70 33
22 41 48 72 33 47 32 37 16 94 29
23 53 71 44 65 25 43 91 52 97 51 14
24 70 11 33 28 77 73 17 78 39 68 17 57
25 91 71 52 38 17 14 91 43 58 50 27 29 48
26 63 66 04 68 89 53 67 30 73 16 69 87 40 31
27 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
28
29 NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
30 '''
31
32 triangle = (
33     (75,                                                         ),
34     (95, 64,                                                     ),
35     (17, 47, 82,                                                 ),
36     (18, 35, 87, 10,                                             ),
37     (20,  4, 82, 47, 65,                                         ),
38     (19,  1, 23, 75,  3, 34,                                     ),
39     (88,  2, 77, 73,  7, 63, 67,                                 ),
40     (99, 65,  4, 28,  6, 16, 70, 92,                             ),
41     (41, 41, 26, 56, 83, 40, 80, 70, 33,                         ),
42     (41, 48, 72, 33, 47, 32, 37, 16, 94, 29,                     ),
43     (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,                 ),
44     (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,             ),
45     (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,         ),
46     (63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,     ),
47     ( 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23, ),
48 )
49
50 def path(triangle, num):
51     s = triangle[0][0]
52     col = 0
53     for row in xrange(1, len(triangle)):
54         if num % 2: col = col + 1
55         num = num / 2
56         s = s + triangle[row][col]
57     return s
58
59 print max(path(triangle, n) for n in xrange(0, 16384))
