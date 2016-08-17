1 '''
 2 What is the first term in the Fibonacci sequence to contain 1000 digits
 3 '''
 4
 5 import math
 6 phi = (1 + pow(5, 0.5)) / 2
 7 c = math.log10(5) / 2
 8 logphi = math.log10(phi)
 9 n = 1
10 while True:
11     if n * logphi - c >= 999:
12         print n
13         break
14     n = n + 1