"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

#1366

import math
import time
start = time.time()

#Madayang Solution
print(sum(int(i) for i in str(2**1000)))

#time: 0.0000s
print('time: {0:.4f}s'.format(time.time()-start))


#pattern finding para sa di madayang solution, kaso wala...
#string manip lang talaga mas madaling sol :(
"""
2**0 =     001  =     1
2**1 =     002  =     2
2**2 =     004  =     4
2**3 =     008  =     8 
2**4 =     016  =    10  =    7
2**5 =     032  =    20  =    5
2**6 =     064  =    40  =   10
2**7 =     128  =    80  =   11
2**8 =     256  =   100  =   13
2**9 =     512  =   200  =    8
2**10 =   1024  =   400  =    7
2**11 =   2048  =   800  =   14
2**12 =   4096  =  1000  =   19 
2**13 =   8192  =  2000  =   20
2**14 =  16384  =  4000  =   22
2**15 =  32768  =  8000  =   26

math.foor((x/4)/10)
2**((x%4))

"""
