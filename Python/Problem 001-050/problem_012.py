"""
Problem 12
The sequence of triangle numbers is generated
by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number
to have over five divisors.

What is the value of the first triangle number
to have over five hundred divisors?
"""

#76576500

import math
import time
start = time.time()

num=7
ans=28
tot=28

fac=[]
while True:
    high = math.floor(math.sqrt(tot))
    #print('tot: {}'.format(tot))
    tot=ans

    i=2
    cr=0
    prv=2
    while tot>=i*i:
        if tot%i==0:
            cr+=1
            tot/=i
        else:
            if cr>0:
                fac.append([cr,i])
                cr=0
            prv=i
            i+= 2 if i>2 else 1
 
    if cr>0:
        fac.append([cr,i])    
    
    if tot>i:
        fac.append([1,tot])
        
    cnt = 1
    
    for x,y in fac:
        cnt *= x+1
        
    if cnt>500:
        #print('tot: {} {}'.format(ans,fac))
        print('tot: {}'.format(ans))
        break
    num+=1
    ans+=num
    fac.clear()

#time: 1.0823s
 
print('time: {0:.4f}s'.format(time.time()-start))


"""
#OLD solution
num=7
tot=28
cnt=2

while True:
    high = math.floor(math.sqrt(tot))
    for i in reversed(range(2,high+1)):
        if tot%i==0:
            #print('{} {}'.format(i,tot/i))
            cnt+=2
            if i==tot/i:
                cnt-=1
                
    #print(cnt)
    
    if cnt>500:
        print(tot)
        break
    num+=1
    tot+=num
    cnt=2

#time: 9.3128s    
""" 
















