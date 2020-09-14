st=''
f=open("problem_008_data.txt","rt")
for x in f:
    st+=x

f.close()
st=''.join(st.split())
print(st)
