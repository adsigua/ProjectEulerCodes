"""
Problem 4
A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#906609

import math



def isPalindrome(num):
    a=str(math.floor(num/1000))
    b=str(num%1000)
    return a==b[::-1]


def isDivBy3(num):
    for i in reversed(range(100,999)):
        f=num/i
        if f%1==0:
            if f>99 and f<1000:
                return True
    return False
    

for x in reversed(range(10000,997799)):
    if isPalindrome(x):
        if isDivBy3(x):
            print(x)
            break

