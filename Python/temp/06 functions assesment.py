#WARMUP section

#LESSER OF TWO EVENS: Write a function that returns
#the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd

#ANIMAL CRACKERS: Write a function takes a two-word string
#and returns True if both words begin with same letter

#MAKES TWENTY: Given two integers, return True if the sum
#of the integers is 20 or if one of the integers is 20.
#If not, return False

def lesser_of_two(a,b):
    if a%2==0 and b%2==0:
        return a if a<b else b
    else:
        return a if a>b else b

def animal_crackers(txt):
    st = txt.split()
    return st[0][0]==st[1][0]

def makes_twenty(n1,n2):
    return n1+n2==20 or n1==20 or n2==20


a = [[1,2],[3,6],[2,4],[2,5],[5,2],[6,2]]
for i in a:
    print(lesser_of_two(i[0],i[1]))

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

print(makes_twenty(20,10))
print(makes_twenty(15,5))
print(makes_twenty(10,1))
print(makes_twenty(12,9))


#Level 1 problems

#OLD MACDONALD: Write a function that capitalizes the
#first and fourth letters of a name


def old_macdonald(name):
    st=[]
    for i in enumerate(name):
        if(i[0]==0 or i[0]==3):
            st.append(i[1].capitalize())
        else:
            st.append(i[1])
    return ''.join(st)


print(old_macdonald('macdonald'))

















