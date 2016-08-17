1 '''
 2 In England the currency is made up of pound, P, and pence, p, and there are eight coins in general circulation:
 3
 4 1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
 5 It is possible to make P2 in the following way:
 6
 7 1 P1 + 1 50p + 2 20p + 1 5p + 1 2p + 3 1p
 8 How many different ways can P2 be made using any number of coins?
 9 '''
10
11 coins = (1, 2, 5, 10, 20, 50, 100, 200)
12
13 def balance(pattern): return sum(coins[x]*pattern[x] for x in xrange(0, len(pattern)))
14
15 def gen(pattern, coinnum, num):
16     coin = coins[coinnum]
17     for p in xrange(0, num/coin + 1):
18         newpat = pattern[:coinnum] + (p,)
19         bal = balance(newpat)
20         if bal > num: return
21         elif bal == num: yield newpat
22         elif coinnum < len(coins)-1:
23             for pat in gen(newpat, coinnum+1, num):
24                 yield pat
25
26 print sum(1 for pat in gen((), 0, 200))