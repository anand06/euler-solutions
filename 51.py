1 '''
 2 By replacing the 1st digit of *57, it turns out that six of the possible values: 157, 257, 457, 557, 757, and 857, are all prime.
 3
 4 By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
 5
 6 Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
 7 '''
 8
 9 import prime
10 from combinatorics import uniqueCombinations
11
12 cache = {}
13 def prime_family_length(n, digits):
14     if cache.has_key((n, digits)): return cache[n, digits]
15
16     num, nums, count = list(str(n)), [], 0
17     if len(dict.fromkeys(num[d] for d in digits).keys()) > 1:
18         return cache.setdefault((n, digits), 0)                                # The digits must have the same number
19
20     for d in range(0 in digits and 1 or 0, 10):                                 # Ensure 0 is not the first digit
21         for x in digits: num[x] = str(d)
22         n = int(''.join(num))
23         if prime.isprime(n): count += 1
24         nums.append(n)
25     for n in nums: cache[n, digits] = count
26     return count
27
28 prime._refresh(100000)
29
30 n, max, max_count, combos = 10, 0, 0, {}
31 while max_count < 8:
32     p = prime.prime(n)
33     digits = range(0, len(str(p)))
34     for size in xrange(1, len(digits)):
35         patterns = combos.setdefault((len(digits), size),
36             tuple(tuple(sorted(p)) for p in uniqueCombinations(digits, size)))
37         for pat in patterns:
38             count = prime_family_length(p, pat)
39             if count > max_count: max, max_count = p, count
40     n += 1
41
42 print p