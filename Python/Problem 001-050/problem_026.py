"""
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators 2 to
10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit
recurring cycle. It can be seen that 1/7 has a 6-digit
recurring cycle.

Find the value of d < 1000 for which 1/d contains the
longest recurring cycle in its decimal fraction part.
"""

#983

import math
import time
start = time.time()

largest=[0,0]
lenght=0
for i in range(11,1000):
    num=10
    stck=[1,10]
    toBreak = False
    while True:
        if i>num:
            num*=10
        elif i%num==0:
            lenght=0
            break
        stck.append(num%i)
        num=num%i

        if stck[len(stck)-1] in stck[:len(stck)-1]:
            length=len(stck[stck.index(stck[len(stck)-1]):len(stck)-1])
            if length > largest[1]:
                largest=[i,length]
            break

print(largest)

#time: 0.6084s

print('time: {0:.4f}s'.format(time.time()-start))



'''  
        for j in range(0,len(stck)-1):
            if stck[j]==stck[len(stck)-1]:
                length=len(stck[j:len(stck)])
                if length > largest[1]:
                    largest=[i,length]
                    #print(i)
                toBreak = True
                break
        if toBreak:
            break

#time: 5.9129s 
'''



'''
stt = '11524552455245'
st=''

ptt={}
ctt={}
for i in range(0,len(stt)):
    brk=False
    for j in [x for x in range(0,i) if st[x]==stt[i]]:
        ptt[st[j:i]]=''
        if st[j:i] not in ctt:
            ctt[st[j:i]]=0
 
    for j in [x for x in ptt]:
        ptt[j]+=stt[i]
        if len(j)==len(ptt[j]) and j==ptt[j]:
            ctt[j]+=1
            ptt[j]==''
            if ctt[j]==2:
                print('ans: {}\n'.format(j))
                brk=True
                break
        elif len(ptt[j])>len(j):
            ctt.pop(j,None)
            ptt.pop(j,None)

    if brk:
        break
    st+=stt[i]
    print('st:{}\nptt{}\n\nctt{}\n'.format(st,ptt,ctt))
'''   


'''
fcList={}
largest = [7,5]
for a in range(900,1000):
    x=1
    st=''
    pattSt=''
    
    ansList=[]
    ptt={}
    ctt={}
    
    while True:
        brk1=False
        ctr=0
        while x<a:
            x*=10
            if x<a:
                st+='0'
                ctr+=1
                
        if x%a==0:
            st+=str(math.floor(x/a))
            x=x%a
            break
        st+=str(math.floor(x/a))
        x=x%a
        ctr+=1

        #print('st:{}  ctr:{}\n'.format(st,ctr))
        
        
        for i in range(len(st)-ctr,len(st)):
            brk2=False
            #print('i:{}'.format(i))
            for j in [x for x in range(0,i) if pattSt[x]==st[i]]:
                ptt[st[j:i]]=''
                if st[j:i] not in ctt:
                    ctt[st[j:i]]=0
         
            for j in [x for x in ptt]:
                ptt[j]+=st[i]
                if len(j)==len(ptt[j]) and j==ptt[j]:
                    ctt[j]+=1
                    ptt[j]==''
                    if ctt[j]==1 and len(j)>2:
                        if len(j) > largest[1]:
                            largest = [a,len(j)]
                        ansList.append(j)
                        brk2=True
                        brk1=True
                        break
                    elif len(j)<=2 and ctt[j]>2:
                        ansList.append(j)
                        brk2=True
                        brk1=True
                        break
                elif len(ptt[j])>len(j):
                    ctt.pop(j,None)
                    ptt.pop(j,None)
            if brk2:
                break
            pattSt+=st[i]
        if brk1:
            break
    print('a:{}  ans:{}\n'.format(a,ansList))

print(largest)

#020408163265306122448979591836734693877551
#020408163265306
'''




