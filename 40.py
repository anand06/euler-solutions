 1 '''
 2 An irrational decimal fraction is created by concatenating the positive integers:
 3
 4 0.123456789101112131415161718192021...
 5
 6 It can be seen that the 12th digit of the fractional part is 1.
 7
 8 If dn represents the nth digit of the fractional part, find the value of the following expression.
 9
10 d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
11
12 0 digit < 1
13 1 digit < + 9 * 1           10
14 2 digit < + 90 * 2          190
15 3 digit < + 900 * 3         2890
16 4 digit < + 9000 * 4
17 5 digit < + 90000 * 5
18 '''
19
20 def digit_at(n):
21     digits = 1
22     n = n - 1
23     while True:
24         numbers = 9 * pow(10, digits-1) * digits
25         if n > numbers: n = n - numbers
26         else: break
27         digits = digits + 1
28     num = n / digits + pow(10, digits-1)
29     return int(str(num)[n % digits])
30
31 print digit_at(1) * digit_at(10) * digit_at(100) * digit_at(1000) * digit_at(10000) * digit_at(100000) * digit_at(1000000)