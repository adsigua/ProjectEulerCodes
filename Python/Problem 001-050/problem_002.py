"""
Problem 2
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum
of the even-valued terms.
"""

#4613732

import math
import time
start = time.time()

ans = 0
prv = 1
nxt = 1
while True:
    tmp=nxt
    nxt+=prv
    prv=tmp
    if nxt>4000000:
        break
    #print(nxt)
    if nxt%2==0:
        ans+=nxt
        
print(ans)
print('time: {0:.4f}s'.format(time.time()-start))
