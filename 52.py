1 '''
 2 It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
 3
 4 Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
 5 '''
 6
 7 def multiples_have_same_digits(n):
 8     digit_keys = dict.fromkeys(list(str(n)))
 9     for x in xrange(2, 4):
10         for d in list(str(x * n)):
11             if not digit_keys.has_key(d): return False
12     return True
13
14 n = 0
15 while True:
16     n = n + 9                           # n must be a multiple of 9 for this to happen
17     if multiples_have_same_digits(n):
18         print n
19         break