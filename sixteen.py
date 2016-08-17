 1 '''
 2 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
 3 What is the sum of the digits of the number 2^1000?
 4 '''
 5
 6 def digits(n):
 7     s = 0
 8     while n > 0:
 9         s = s + (n % 10)
10         n = n / 10
11     return s
12
13 print digits(pow(2,1000))