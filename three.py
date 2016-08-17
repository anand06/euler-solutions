 1 '''
 2 The prime factors of 13195 are 5, 7, 13 and 29.
 3
 4 What is the largest prime factor of the number 600851475143 ?
 5 '''
 6
 7 n = 600851475143
 8 i = 2
 9 while i * i < n:
10     while n % i == 0:
11         n = n / i
12     i = i + 1
13
14 print n