"""
Problem 17
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters
would be used?


NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
"""

#21124

import math
import time
start = time.time()

numLet = {
    1:3,#len('one'),
    2:3,#len('two'),
    3:5,#len('three'),
    4:4,#len('four'),
    5:4,#len('five'),
    6:3,#len('six'),
    7:5,#len('seven'),
    8:5,#len('eight'),
    9:4,#len('nine'),
    10:3,#len('ten'),
    11:6,#len('eleven'),
    12:6,#len('twelve'),
    13:8,#len('thirteen'),
    14:8,#len('fourteen'),
    15:7,#len('fifteen'),
    16:7,#len('sixteen'),
    17:9,#len('seventeen'),
    18:8,#len('eighteen'),
    19:8,#len('nineteen'),
    20:6,#len('twenty'),
    30:6,#len('thirty'),
    40:5,#len('forty'),
    50:5,#len('fifty'),
    60:5,#len('sixty'),
    70:7,#len('seventy'),
    80:6,#len('eighty'),
    90:6,#len('ninety'),
    100:7,#len('hundred'),
    1000:8#len('thousand')
    }

st=0
for i in range(1,1000):
    x=i
    ss=st
    if x>=100:
        st+=numLet[math.floor(x/100)]+numLet[100]
        if x%100>0:
            st+=3#and
        x%=100
    if x>=20:
        st+=numLet[math.floor(x/10)*10]
        x%=10
    if x<20 and x>0:
        st+=numLet[x]
    
    #print('{} {}'.format(i,st-ss))
        
st+=numLet[1000]+numLet[1]
print(st)
    
print('time: {0:.4f}s'.format(time.time()-start))

#time: 0.0050s


