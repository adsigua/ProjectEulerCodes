"""
Let d(n) be defined as the sum of proper divisors
of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

#31626

import math
import time
start = time.time()


tot=0
numL=[[1] for x in range(0,10000)]
pairL={}
for i in range(2,10000):
    ss = sum(numL[i])
    if ss in pairL and pairL[ss]==i:
        tot+=i+ss
        continue
    else:
        if ss>1:
            pairL[i] = ss
        x=2 
        while i*x<10000:
            numL[i*x].append(i)
            x+=1


print(tot)

print('time: {0:.4f}s'.format(time.time()-start))

#time: 0.0469s










