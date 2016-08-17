1 '''
 2 A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
 3
 4 012   021   102   120   201   210
 5
 6 What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 7 '''
 8
 9 def fact(n):
10     f = 1
11     for x in xrange(1, n+1): f = f * x
12     return f
13
14 def permutation(orig_nums, n):
15     nums = list(orig_nums)
16     perm = []
17     while len(nums):
18         divider = fact(len(nums)-1)
19         pos = n / divider
20         n = n % divider
21         perm.append(nums[pos])
22         nums = nums[0:pos] + nums[pos+1:]
23     return perm