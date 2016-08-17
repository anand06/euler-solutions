1 '''
 2 The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
 3
 4 We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
 5
 6 There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
 7
 8 If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
 9 '''
10
11 def fractions():
12     for numerator in map(str, xrange(10, 100)):
13         for denominator in map(str, xrange(int(numerator)+1, 100)):
14             if numerator == denominator: continue
15             if numerator[1] == denominator[1] and numerator[1] == '0': continue
16             if numerator[0] == denominator[0] and int(numerator) * int(denominator[1]) == int(denominator) * int(numerator[1]): yield(int(numerator), int(denominator))
17             if numerator[0] == denominator[1] and int(numerator) * int(denominator[0]) == int(denominator) * int(numerator[1]): yield(int(numerator), int(denominator))
18             if numerator[1] == denominator[1] and int(numerator) * int(denominator[0]) == int(denominator) * int(numerator[0]): yield(int(numerator), int(denominator))
19             if numerator[1] == denominator[0] and int(numerator) * int(denominator[1]) == int(denominator) * int(numerator[0]): yield(int(numerator), int(denominator))
20
21 def gcd(a,b): return b and gcd(b, a % b) or a
22
23 numerator = 1
24 denominator = 1
25 for frac in fractions():
26     numerator = numerator * frac[0]
27     denominator = denominator * frac[1]
28
29 g = gcd(numerator, denominator)
30 print denominator / g