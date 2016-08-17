1 '''
 2 The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
 3
 4 Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
 5
 6 NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
 7 '''
 8
 9 import math, prime
10
11 digits = range(0, 10)
12 prime_digits = (2, 3, 5, 7)
13
14 def num(l):
15     s = 0
16     for n in l: s = s * 10 + n
17     return s
18
19 def is_left_truncatable(l):
20     is_truncatable = 1
21     for size in xrange(1, len(l)+1):
22         n = num(l[:size])
23         prime._refresh(int(math.sqrt(n)))
24         if not prime._isprime(n):
25             is_truncatable = 0
26             break
27     return is_truncatable
28
29 def is_right_truncatable(l):
30     is_truncatable = 1
31     for size in xrange(0, len(l)):
32         n = num(l[size:])
33         prime._refresh(int(math.sqrt(n)))
34         if not prime._isprime(n):
35             is_truncatable = 0
36             break
37     return is_truncatable
38
39 def gen(result, number):
40     if len(number) > 6: return
41     number = list(number)
42     number.append('')
43     for digit in digits:
44         number[-1] = digit
45         if is_left_truncatable(number):
46             if is_right_truncatable(number) and len(number) > 1:
47                 result.append(num(number))
48             gen(result, number)
49
50 result = []
51 gen(result, [])
52 print sum(result)