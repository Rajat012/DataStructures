
# Pivot element as first

def pivot_index(list1,first,last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while(left<=right and list1[left]<=pivot):
            left=left+1
        while(left<=right and list1[right]>=pivot):
            right=right-1
        if(left>right):
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right    
    
def quicksort(list1,first,last):
    if(first<last):
        pivot=pivot_index(list1,first,last)
        quicksort(list1,first,pivot-1)
        quicksort(list1,pivot+1,last)
 
size=int(input("Enter Size : "))
list1=[int(input("")) for i in range(size)]
quicksort(list1,0,size-1)
print(list1)


# pivot Element as last
'''
def pivot_index(list1,first,last):
    pivot=last
    left=first
    right=last-1
    while True:
        while(left<=right and list1[left]<=list1[pivot]):
            left+=1
        while(left<=right and list1[right]>=list1[pivot]):
            right-=1
        if(left>right):
            break
        else:list1[right],list1[left]=list1[left],list1[right]
    list1[left],list1[pivot]=list1[pivot],list1[left] 
    return left

def quicksort(list1,first,last):
    if(first<last):
        pivot=pivot_index(list1,first,last)
        quicksort(list1,first,pivot-1)
        quicksort(list1,pivot+1,last)
        
size=int(input("Enter Size : "))
list1=[int(input("")) for i in range(size)]
quicksort(list1,0,size-1)
print(list1)  
'''


# Random index QuickSort
'''
import random

def pivot_index(list1,first,last):
    r_index=random.randint(first,last)
    list1[r_index],list1[last]=list1[last],list1[r_index]
    pivot=last
    left=first
    right=last-1
    while True:
        while(left<=right and list1[left]>=list1[pivot]):
            left+=1
        while(left<=right and list1[right]<=list1[pivot]):
            right-=1
        if(left>right):
            break
        else:list1[right],list1[left]=list1[left],list1[right]
    list1[left],list1[pivot]=list1[pivot],list1[left] 
    return left

def quicksort(list1,first,last):
    if(first<last):
        pivot=pivot_index(list1,first,last)
        quicksort(list1,first,pivot-1)
        quicksort(list1,pivot+1,last)
        
size=int(input("Enter Size : "))
list1=[int(input("")) for i in range(size)]
quicksort(list1,0,size-1)
print(list1)       
'''


# Median QuickSort
'''
import statistics

def pivot_index(list1,first,last):
    low=list1[first]
    high= list1[last]
    mid=(first+last)//2
    median=statistics.median([low,list1[mid],high])
    if median==low:
        median_index=first
    elif median==high:
        median_index=last
    else:
        median_index=mid
    list1[median_index],list1[last]=list1[last],list1[median_index]
    
    pivot=last
    left=first
    right=last-1
    while True:
        while(left<=right and list1[left]>=list1[pivot]):
            left+=1
        while(left<=right and list1[right]<=list1[pivot]):
            right-=1
        if(left>right):
            break
        else:list1[right],list1[left]=list1[left],list1[right]
    list1[left],list1[pivot]=list1[pivot],list1[left] 
    return left

def quicksort(list1,first,last):
    if(first<last):
        pivot=pivot_index(list1,first,last)
        quicksort(list1,first,pivot-1)
        quicksort(list1,pivot+1,last)
        
size=int(input("Enter Size : "))
list1=[int(input("")) for i in range(size)]
quicksort(list1,0,size-1)
print(list1)       
'''
