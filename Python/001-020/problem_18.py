
#1074

import time
startTime = time.time()

numList=[]
ff=open('data2.txt','r')
for st in ff:
    numList.append([int(x) for x in st.split()])
ff.close()

#print(numList)
#print(len(numList))

for i in reversed(range(0,len(numList)-1)):
    for j in range(0,len(numList[i])):
        numList[i][j]+=numList[i+1][j] if numList[i+1][j]>numList[i+1][j+1] else numList[i+1][j+1]

print(numList[0][0])

print('time: {}s'.format(time.time()-startTime))
