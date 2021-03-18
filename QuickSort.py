
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
  
