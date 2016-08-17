
 1 '''
 2 The sum of the squares of the first ten natural numbers is,
 3 1^2 + 2^2 + ... + 10^2 = 385
 4 The square of the sum of the first ten natural numbers is,
 5 (1 + 2 + ... + 10)^2 = 552 = 3025
 6 Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
 7
 8 Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 9 '''
10
11 r = xrange(1, 101)
12 a = sum(r)
13 print a * a - sum(i*i for i in r)