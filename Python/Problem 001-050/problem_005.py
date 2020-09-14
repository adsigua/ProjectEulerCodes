"""
Problem 5
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""


#232792560

import math

upper = 3724680960
lower = 9699690


def isDivByAll(num):
    return (num%11==0 and num%13==0  and num%14==0
            and num%16==0  and num%17==0  and num%18==0  and num%19==0
            and num%20==0)    


num=0
for i in range(lower,upper,9699690):
    num+=1
    if isDivByAll(i):
        print('answer:{}'.format(i))
        print('iterations:{}'.format(num))
        break


