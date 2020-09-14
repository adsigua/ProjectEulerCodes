"""
Work out the first ten digits of the sum of the
following one-hundred 50-digit numbers.

problem_013_data.txt

"""

#5537376230

import math
import time
start = time.time()

stList=[]
f=open("problem_013_data.txt","rt")
for x in f:
    st = x.replace('\n','')
    stList.append(st)

f.close()
#print(stList)

tot=0
carry=0
for a in reversed(range(10,50)):
    tot=carry
    carry=0
    for b in stList:
        tot+=int(b[a])
    carry=math.floor(tot/10)

tot = carry*10
for a in reversed(range(0,10)):
    for b in stList:
        tot+=int(b[a])*((10)**(10-a))
        
while tot>(10**10):
    tot=math.floor(tot/10)

print(tot)


print('time: {0:.4f}s'.format(time.time()-start))

#time: 0.0350s



