"""
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate
the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#837799

import math
import time
start = time.time()

num={}

def getCount(x):
    if not x in num:
        num[x]=0
    if num[x]>0:
        return num[x]
    i = x/2 if x%2==0 else (3*x)+1
    num[x] = getCount(int(i))+1
    return num[x]



num[1]=1
largest = 1
for i in range(1,1000000):
    if not i in num:
        num[i] = getCount(i)
        if num[i]>num[largest]:
            largest = i

print('largest: {} count: {}'.format(largest,num[largest]))
print('time: {0:.4f}s'.format(time.time()-start))

#time: 3.0314s


"""
num={}

num[1]=1
largest = 1
for i in range(1,1000001):
    if not i in num:
        x=i
        ind=[x]
        while x not in num:
            if x%2==0:
                x = int(x/2)
            else:
                x = int((3*x)+1)
            #x = int(x/2) if x%2==0 else int((3*x)+1)
            ind.append(x)

        #j = ind.pop()
        count=num[ind.pop()]
        #print('i: {} count: {}'.format(j,count))
        #print(ind)
        for a in reversed(ind):
            count+=1
            num[a]=count
        if num[i]>num[largest]:
            largest = i

print('largest: {} count: {}'.format(largest,num[largest]))
print('time: {0:.4f}s'.format(time.time()-start))

#time: 3.1564s

"""



