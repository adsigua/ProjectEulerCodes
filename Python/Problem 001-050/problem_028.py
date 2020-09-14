"""

"""

#669171001

import math
import time
start = time.time()

#time: 0.0060s

num=1001
i=num*num

total=1
for x in range(3,num,2):
    total+=(4*x*x)-(6*x)+6
print(total)


'''
#time: 0.0070s
total=1
n=num-1
while i>1:
    for x in range(0,4):
        total+=i
        i-=n
    n-=2
print(total)
'''


print('time: {0:.4f}s'.format(time.time()-start))
