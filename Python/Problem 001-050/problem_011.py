"""
In the 20×20 grid below, four numbers along a diagonal 
line have been marked in red.

The product of these numbers is 
26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or 
diagonally) in the 20×20 grid?
"""

#70600674

import math
import time
start = time.time()

nums=[]
f=open("problem_011_data.txt","rt")
for x in f:
    row=[]
    for y in x.split():
        row.append(int(y))
    nums.append(row)
f.close()



largest=0

#check vertical
for a in range(3,20,6):
    for b in range(0,20):
        for i in [a+x for x in range(-3,0) if a+x>=0 and a+x+3<20]:
            prod = nums[i][b]*nums[i+1][b]*nums[i+2][b]*nums[i+3][b]
            largest = prod if prod > largest else largest        

        #check diagonal_backSlash
        for i in [a+x for x in range(-3,0) if a+x>=0 and a+x+3<20]:
            for j in [b+x for x in range(-3,0) if b+x>=0 and b+x+3<20]:
                prod = nums[i][j]*nums[i+1][j+1]*nums[i+2][j+2]*nums[i+3][j+3]
                largest = prod if prod > largest else largest

        #check diagonal 
        for i in [a+x for x in range(-3,0) if a+x>=0 and a+x+3<20]:
            for j in [b-x for x in range(-3,0) if b-x-3>=0 and b-x<20]:
                prod = nums[i][j]*nums[i+1][j-1]*nums[i+2][j-2]*nums[i+3][j-3]
                largest = prod if prod > largest else largest

#check horizontal        
for i in range(3,20,6):
    for j in range(0,20):
        for k in [i+x for x in range(-3,0) if i+x>=0 and i+x+3<20]:
            prod = nums[j][k]*nums[j][k+1]*nums[j][k+2]*nums[j][k+3]
            largest = prod if prod > largest else largest


print(largest)

#time: 0.0313s

print('time: {0:.4f}s'.format(time.time()-start))




