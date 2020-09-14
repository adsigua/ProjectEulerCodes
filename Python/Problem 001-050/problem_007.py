"""
Problem 7
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

#104743

import math
import time
start = time.time()

def isPrime(x):
    for i in range(3,int(math.floor(math.sqrt(x)))+1,2):
        if x%i==0:
            return False
    return True

x=3
cnt=1
while cnt<10001:
    #fc=math.factorial(x-1)
    #if(fc%x==x-1):
    if(isPrime(x)):
        cnt+=1
    x+=2
print(x-2)




print('time: {0:.4f}s'.format(time.time()-start))
