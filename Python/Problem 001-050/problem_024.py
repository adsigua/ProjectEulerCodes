"""
Problem 24
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or
alphabetically, we call it lexicographic order. The lexicographic
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

#2783915460

import math
import time
start = time.time()

st='0123456789'

cnt=999999
for i in range(0,9):
    fc = math.factorial(9-i)
    offSet = 0
    #print('fc:{}  cnt:{}'.format(fc,cnt))
    while cnt>=fc:
        cnt-=fc
        offSet+=1
    stt=''
    if i > 0:
        stt = st[0:i]
    st = stt + st[i+offSet] + st.replace(st[i+offSet],'')[i:]
print(st)


print('time: {0:.4f}s'.format(time.time()-start))

#time: 0.0523s

#637120
#274240
#off = 2

#9! = 362880

#274240/8! = 6
#8!=40320*6 = 241920
#32320

#7!=540
#6!=720
#i= 362880 + 362880

