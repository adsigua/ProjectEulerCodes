"""
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible
by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which
produces 80 primes for the consecutive values 0≤n≤79. The product of
the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for
the quadratic expression that produces the maximum number
of primes for consecutive values of n, starting with n=0.
"""

#

import math
import time
start = time.time()

#numList = [range(-1000,1000),range(-999,999,2)]
#print(numList)

def isPrime(x):
    if x<3 or x%2==0:
        return False
    
    for i in range(3,int(math.floor(math.sqrt(x)))+1,2):
        if x%i==0:
            return False
    return True

'''
primeList = []
for i in range(3,2001001,2):
    if(isPrime(i)):
        primeList.append(i)

print(len(primeList))
print('time: {0:.4f}s'.format(time.time()-start))
start = time.time()
'''

bVal=[]
b=3
numsList=[]
for b in range(3,1000,2):
    if(isPrime(b)):
        for a in range(-1000,1000):
            x=1+b+a
            if(x>0 and x%2!=0):
                if(isPrime(x)):
                    numsList.append([a,b])
'''
print('time: {0:.4f}s'.format(time.time()-start))
start = time.time()
'''
n=2
while (len(numsList)>1):
    removeList = []
    for nums in numsList:
        x = (n*n) + (n*nums[0]) + nums[1]
        if(x>0 and x%2!=0):
            if(not isPrime(x)):
                removeList.append(nums)
            else:
                continue
        else:
            removeList.append(nums)
            
    for nums in removeList:
        numsList.remove(nums)
    n+=1

print(numsList)
print(numsList[0][0]*numsList[0][1])


'''
while(len(numsList)>1):
    for nums in numsList:
        x = (n*n) + (n*nums[0]) + nums[1]
        if(x>0 and x%2!=0):
            if(~isPrime(x)):
                numsList.remove(nums)
                print(len(numsList))
            else:
                print(nums)
    n+=1
'''


'''
for b in range(-999,1001,2):
    for a in range(-1000,1000):
        upLim = math.abs(b) if math.abs(a)>math.abs(b) else math.abs(a)
        for n in range(0,upLim)
        pass

'''



print('time: {0:.4f}s'.format(time.time()-start))




