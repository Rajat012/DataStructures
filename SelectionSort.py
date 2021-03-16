no= int(input("Enter Total No. of Elements : "))
list1=[int(input("")) for i in  range(no)]
print("Unsorted List : ",list1)

for i in range(0,len(list1)):
    min_val=list1[i]
    for j in range(i,len(list1)-1):
        if(min_val>list1[j+1]):
            list1[i],list1[j+1]=list1[j+1],list1[i]
            min_val=list1[i]
print("Sorted List : ",list1)            
