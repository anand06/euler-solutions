 1 '''
 2 You are given the following information, but you may prefer to do some research for yourself.
 3
 4 1 Jan 1900 was a Monday.
 5 Thirty days has September,
 6 April, June and November.
 7 All the rest have thirty-one,
 8 Saving February alone,
 9 Which has twenty-eight, rain or shine.
10 And on leap years, twenty-nine.
11 A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
12
13 How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
14 '''
15 import datetime
16
17 sundays = 0
18 for year in xrange(1901, 2001):
19     for month in xrange(1, 13):
20         d = datetime.date(year, month, 1)
21         if d.weekday() == 6:
22             sundays = sundays + 1
23
24 print sundays