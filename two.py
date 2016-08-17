 1 '''
 2 Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
 3
 4 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 5
 6 Find the sum of all the even-valued terms in the sequence which do not exceed four million.
 7 '''
 8
 9 cache = {}
10 def fib(n):
11     cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fib(n-1) + fib(n-2))
12     return cache[n]
13
14 n = 0
15 i = 0
16 while fib(i) <= 4000000:
17     if not fib(i) % 2: n = n + fib(i)
18     i = i + 1
19
20 print n