"""
Starting in the top left corner of a 2×2 grid, and only
being able to move to the right and down, there
are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

#137846528820

import math
import time
start = time.time()


size=20

grid=[[0 for j in range(0,size+1)] for x in range(0,size+1)]
grid[0][0]=1


for i in range(0,size+1):
    for j in range(0,size+1):
        if i==0 and j==0:
            continue
        if j-1>=0:
            grid[i][j]+=grid[i][j-1]
        if i-1>=0:
            grid[i][j]+=grid[i-1][j] 
     
print(grid[size][size])
print('time: {0:.4f}s'.format(time.time()-start))

#time: 0.0156s
