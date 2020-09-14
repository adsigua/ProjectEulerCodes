"""
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

#31875000

import math
import time
start = time.time()


for b in [x for x in reversed(range(2,499))]:
    a=((500000-(1000*b))/(1000-b))
    c=((500000-(1000*b)+(b*b))/(1000-b))
    if a%1==0 and c%1==0 and  b < c and b > a:
    
        print('{}*{}*{} = {}'.format(a,b,c,math.floor(a*b*c)))
        
print('time: {0:.4f}s'.format(time.time()-start))
