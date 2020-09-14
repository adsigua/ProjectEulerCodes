"""
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the
sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""

#25164150

import math
import time

start = time.time()
totS=385
tot=55
for x in range(11,101):
    totS+=x*x
    tot+=x

diff = (tot*tot)-totS
print(diff)

print('time: {0:.4f}s'.format(time.time()-start))
