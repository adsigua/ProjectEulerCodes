import math

nums = [38, 27, 43, 3, 9, 82, 10]

def partition(arr,start,end):
    pivot = arr[end]
    pindex = start

    for i in range(start,end):
        if(arr[i]<=pivot):
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    
    return pindex

def quickSort(arr,start,end):
    if(start>=end):
        return
    print('array: {}'.format(arr))
    pivot = partition(arr,start,end)

    quickSort(arr,start,pivot-1)
    quickSort(arr,pivot+1,end)
    

def merge(arr, low, mid, high):
    n1 = mid-low+1
    n2 = high-mid
    l = [arr[low+x] for x in range(0,n1)]
    r = [arr[mid+x+1] for x in range(0,n2)]
    i=0
    j=0
    k=low
    while(i < n1 and j < n2):

        if(l[i] <= r[j]):
            arr[k]=l[i]
            i+=1
        else:
            arr[k]=r[j]
            j+=1
        k+=1
    while(i < n1):
        arr[k]=l[i]
        k+=1
        i+=1
        
    while(j < n2):
        arr[k]=r[j]
        k+=1
        j+=1

    print('array: {}'.format(arr))

def merge_sort(arr, low, high):
    if(high==low):
        return
    nums = arr
    mid = math.floor((low + ((high-low) / 2)))

    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)

    merge(arr,low,mid,high)


qckNums=[x for x in nums]
quickSort(qckNums,0,len(qckNums)-1)
print(qckNums)
print('nums:{}'.format(nums))
mrgNums=[x for x in nums]
merge_sort(mrgNums,0,len(mrgNums)-1)
print(mrgNums)

