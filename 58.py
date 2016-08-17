 1 '''
 2 Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
 3
 4 37 36 35 34 33 32 31
 5 38 17 16 15 14 13 30
 6 39 18  5  4  3 12 29
 7 40 19  6  1  2 11 28
 8 41 20  7  8  9 10 27
 9 42 21 22 23 24 25 26
10 43 44 45 46 47 48 49
11
12 It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
13
14 If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
15 '''
16
17 import prime
18 prime._refresh(50000)
19
20 width, diagonal, base, primes = 1, 1, 1, 0
21 while True:
22     width = width + 2
23     increment = width - 1
24     for i in xrange(0, 4):
25         diagonal = diagonal + increment
26         if i < 3 and prime._isprime(diagonal): primes += 1
27     base = base + 4
28     if primes * 10 < base:
29         print width
30         break