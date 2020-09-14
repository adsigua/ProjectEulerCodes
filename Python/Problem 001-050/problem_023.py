"""
Problem 23
A perfect number is a number for which the sum of
its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of its
proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be
shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two
abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.
"""

#4179871

import math
import time
start = time.time()

fac = [[1] for x in range(0,28124)]
#numL = [x for x in range(1,28124)]
abNums = []
abSums = {}
tot=0

def isAbundant(x):
    ss=1
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x%i == 0:
           ss += i
           d = x/i
           if d!=i:
              ss+=d
    return ss>x  

stt = time.time()
for i in range(12,28124):
    if isAbundant(i):
        abNums.append(i)
        #print(i)


isSumOfAbNums = [False]*(28123*2)

for a in range(0,len(abNums)):
    for b in range(0,a+1):
        isSumOfAbNums[abNums[a]+abNums[b]]=True


#print(sum(i for i in range(1,28124) if not any(i-a for a in abNums)))

print(sum([x for x in range(1,28124) if not isSumOfAbNums[x]]))        
print('time: {0:.4f}s'.format(time.time()-stt))


#time: 7.2506s

'''       
for i in range(24,28124):
    for b in abNums:
        if b>i/2:
            break
        if i-b in abNums:
            tot-=i
            #print(i)
            break
print(tot)

print('time: {0:.4f}s'.format(time.time()-start))

'''


