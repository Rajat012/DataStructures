
def quicksort(list1):
    if len(list1)<=1:
        return list1
    
    pivot=list1[0]
    list1=list1[1::]
    
    lower=[]
    greater=[]
    
    for i in list1:
        if i<=pivot:
            lower.append(i)
        else:
            greater.append(i)
    
    sorted_list=quicksort(lower) + [pivot] + quicksort(greater)
    return sorted_list
    
size=int(input("Enter Size : "))
list1=[int(input("")) for i in range(size)]
sorted_list=quicksort(list1)
print(sorted_list)
