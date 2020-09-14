"""
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#6857

import math

def isPrime(x):
    high = math.floor(x/3)
    if x%2==0:
        return False
    for y in range(3,high,2):
        if x%y==0:
            return False
    return True
    

num = 600851475143 
high = math.floor(math.sqrt(num))
if high%2==0:
    high-=1
for x in reversed(range(1,high,2)):
    #print(x)
    if num%x==0 and x%2!=0:
        if isPrime(x):
            print(x)
            break;
