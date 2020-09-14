"""
Problem 8
The four adjacent digits in the 1000-digit
number that have the greatest product
are 9 × 9 × 8 × 9 = 5832.

problem_008_data.txt

Find the thirteen adjacent digits in the
1000-digit number that have the greatest product.
What is the value of this product?

"""

#23514624000

import math
import time
start = time.time()

st=''
f=open("problem_008_data.txt","rt")
for x in f:
    st+=x

f.close()
st=''.join(st.split())
print(st)

largest = 0
for x in range(0,987):
    z=1
    for y in range(0,13):
        z *= int(st[x+y])
      
    largest = z if z>largest else largest

print(largest)
print('time: {0:.4f}s'.format(time.time()-start))
