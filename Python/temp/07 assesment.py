print('PART 1:')
st1 = 'Print only the words that start with s in this sentense'
for x in st1.split():
    if x[0].lower() == 's':
        print(x,end=" ")
    
print('\n\nPART 2:')
for i in range(0,11,2):
    print(i,end=" ")

print('\n\nPART 3:')
for i in [x for x in range(1,51) if x%3==0]:
    print(i,end=" ")

print('\n\nPART 4:')
st2 = 'Print every word in this sentence that has an even number of letters'
for i in [x if (len(x))%2!=0 else 'even!' for x in st2.split()]:
    print(i,end=" ")

print('\n\nPART 5:')
for ind,i in enumerate(['FizzBuzz' if x%15==0 else 'Fizz' if x%3==0 else 'Buzz' if x%5==0 else x for x in range(1,101)]):
    print(i,end=" ")
    if (ind+1)%10==0:
        print('')

print('\n\nPART 6:')
st2 = 'Create a list of the first letters of every word in this string'
for i in [x[0] for x in st2.split()]:
    print(i,end=" ")
