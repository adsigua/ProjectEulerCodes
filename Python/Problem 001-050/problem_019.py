"""
You are given the following information,
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

#171

import math
import time
start = time.time()

y=1900
m=1
d=1
count=1
while y<2001:
    if y==1901:
        count=0
    while m<13:
        if d%7==0:
            count+=1
        if m==2:
            if (y!=0 or y%400==0) and y%4==0:
                d+=29
            else:
                d+=28
        elif m==4 or m==6 or m==9 or m==11:
            d+=30
        else:
            d+=31
        m+=1
    m=1
    y+=1

print(count)

print('time: {0:.4f}s'.format(time.time()-start))


#time: 0.0000s


