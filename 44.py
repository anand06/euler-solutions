1 '''
 2 Pentagonal numbers are generated by the formula, P_n=n(3n-1)/2. The first ten pentagonal numbers are:
 3
 4 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
 5
 6 It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference, 70 - 22 = 48, is not pentagonal.
 7
 8 Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference is pentagonal and D = |P_k - P_j| is minimised; what is the value of D?
 9 '''
10
11 MAX = 2000
12 pent = [ n * (3*n - 1) / 2 for n in xrange(1, 2*MAX) ]
13 pdic = dict.fromkeys(pent)
14
15 def main2():
16     for j in xrange(0, MAX):
17         for k in xrange(j+1, 2*MAX-1):
18             p_j = pent[j]
19             p_k = pent[k]
20             p_sum = p_j + p_k
21             p_diff = p_k - p_j
22             if pdic.has_key(p_sum) and pdic.has_key(p_diff):
23                 return p_diff
24
25 print main2()