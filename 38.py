1 '''
 2 Take the number 192 and multiply it by each of 1, 2, and 3:
 3
 4 192 x 1 = 192
 5 192 x 2 = 384
 6 192 x 3 = 576
 7 By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
 8
 9 The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
10
11 What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
12 '''
13
14 def get_pandigital(n):
15     pandigital = ''
16     for x in xrange(1, 10):
17         pandigital += str(x * n)
18         if len(pandigital) >= 9: break
19     if len(pandigital) == 9 and sorted(dict.fromkeys(list(pandigital)).keys()) == list("123456789"): return pandigital
20     else: return ''
21
22 max = 0
23 for n in xrange(1, 10000):
24     p = get_pandigital(n)
25     if p and p > max: max = p
26