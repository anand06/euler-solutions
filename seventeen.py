tters would be needed to write all the numbers in words from 1 to 1000?
 3 '''
 4
 5 words = [
 6     (   1,  'one'      , ''     ),
 7     (   2,  'two'      , ''     ),
 8     (   3,  'three'    , ''     ),
 9     (   4,  'four'     , ''     ),
10     (   5,  'five'     , ''     ),
11     (   6,  'six'      , ''     ),
12     (   7,  'seven'    , ''     ),
13     (   8,  'eight'    , ''     ),
14     (   9,  'nine'     , ''     ),
15     (  10,  'ten'      , ''     ),
16     (  11,  'eleven'   , ''     ),
17     (  12,  'twelve'   , ''     ),
18     (  13,  'thirteen' , ''     ),
19     (  14,  'fourteen' , ''     ),
20     (  15,  'fifteen'  , ''     ),
21     (  16,  'sixteen'  , ''     ),
22     (  17,  'seventeen', ''     ),
23     (  18,  'eighteen' , ''     ),
24     (  19,  'nineteen' , ''     ),
25     (  20,  'twenty'   , ''     ),
26     (  30,  'thirty'   , ''     ),
27     (  40,  'forty'    , ''     ),
28     (  50,  'fifty'    , ''     ),
29     (  60,  'sixty'    , ''     ),
30     (  70,  'seventy'  , ''     ),
31     (  80,  'eighty'   , ''     ),
32     (  90,  'ninety'   , ''     ),
33     ( 100,  'hundred'  , 'and'  ),
34     (1000,  'thousand' , 'and'  ),
35 ]
36 words.reverse()
37
38 def spell(n, words):
39     word = []
40     while n > 0:
41         for num in words:
42             if num[0] <= n:
43                 div = n / num[0]
44                 n = n % num[0]
45                 if num[2]: word.append(' '.join(spell(div, words)))
46                 word.append(num[1])
47                 if num[2] and n: word.append(num[2])
48                 break
49     return word
50
51 print sum(len(word) for n in xrange(1, 1001) for word in spell(n, words))