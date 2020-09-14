"""
Using problem_22_data.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical
order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a
score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

#871198282

import math
import time
start = time.time()


st=[]
f=open("problem_022_data.txt","rt")
for x in f:
    for y in x.split(','):
        ss=y.replace('"','')
        st.append(ss)
f.close()
st.sort()
#65 = A
tot = 0
for i in range(0,len(st)):
    tot+=sum([ord(x)-64 for x in st[i]])*(i+1)

print(tot)

print('time: {0:.4f}s'.format(time.time()-start))


#time: 0.0240s


