def bubbleSort(x):
    for i in range(0,len(x)-1):
        for y in range(0,len(x)-1):
            if(x[y]>x[y+1]):
                temp=x[y+1]
                x[y+1]=x[y]
                x[y]=temp

    print(x)        
            
x=[9,7,1,6,8,4,3,7]
bubbleSort(x)
