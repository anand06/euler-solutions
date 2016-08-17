 1 '''
 2 The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
 3
 4 Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
 5
 6 HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 7 '''
 8
 9 from combinatorics import permutations
10
11 def num(l):
12     s = 0
13     for n in l: s = s * 10 + n
14     return s
15
16 product = {}
17 for perm in permutations(range(1,10)):
18     for cross in range(1,4):            # Number can't be more than 4 digits
19         for eq in range(cross+1, 6):    # Result can't be less than 4 digits
20             a = num(perm[0:cross])
21             b = num(perm[cross:eq])
22             c = num(perm[eq:9])
23             if a * b == c: product[c] = 1
24
25 print sum(p for p in product)