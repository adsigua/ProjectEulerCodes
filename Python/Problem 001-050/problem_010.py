"""
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#142913828922

import math
import time
start = time.time()


num = [True for i in range(2,2000000)]
for x in [i for i in range(2,math.floor(math.sqrt(2000000))+1)]:
    if num[x-2]:
        i=0
        y=(x*x)
        while y<2000000:
            num[y-2]=False
            i+=1
            y=(x*x)+(x*i)
            
tot=0        
for i in [x for x in range(2,2000000)]:
    if num[i-2]:
        tot+=i
    
print(tot)

print('time: {0:.4f}s'.format(time.time()-start))

#time: 3.1251s
