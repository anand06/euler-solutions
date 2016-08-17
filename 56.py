 1 '''
 2 A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
 3
 4 Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
 5 '''
 6
 7 max = 0
 8 for a in xrange(0, 100):
 9     for b in xrange(0, 100):
10         ds = sum(int(digit) for digit in str(a**b))
11         if ds > max: max = ds
12 print max