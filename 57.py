1 '''
 2 It is possible to show that the square root of two can be expressed as an infinite continued fraction.
 3
 4 sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
 5
 6 By expanding this for the first four iterations, we get:
 7
 8 1 + 1/2 = 3/2 = 1.5
 9 1 + 1/(2 + 1/2) = 7/5 = 1.4
10 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
11 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
12
13 The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
14
15 In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
16 '''
17
18 num, den, count = 3, 2, 0
19 for iter in xrange(0, 1000):
20     num, den = num + den + den, num + den
21     if len(str(num)) > len(str(den)):
22         count += 1
23 print count