arrsize= int(input("size of array : "))
arr1 = [int(input("")) for i in range(arrsize)]
print(arr1)

fincount=0
no=0
for i in range(0,len(arr1)):
    x=arr1[i]
    count=0
    for j in range(i,len(arr1)):
        if(x==arr1[j]):
            count+=1
    if (count>fincount):
            fincount=count
            no=x
    if(count==fincount):
        if(no<x):no=x
print(no,"  ",fincount,"Times")                
