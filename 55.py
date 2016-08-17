1 '''
 2 If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
 3
 4 Not all numbers produce palindromes so quickly. For example,
 5
 6 349 + 943 = 1292,
 7 1292 + 2921 = 4213
 8 4213 + 3124 = 7337
 9
10 That is, 349 took three iterations to arrive at a palindrome.
11
12 Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
13
14 Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
15
16 How many Lychrel numbers are there below ten-thousand?
17
18 NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
19 '''
20
21 def is_lychrel(n):
22     n = str(n)
23     for count in xrange(0, 50):
24         n = str(int(n) + int(n[::-1]))
25         if n == n[::-1]: return False
26     return True
27
28 print sum(1 for n in xrange(0, 10000) if is_lychrel(n))