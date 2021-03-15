x= int(input("Enter NO. : "))
res=1
if(x>=2):
    for i in range(2,x):
        if((x%i)==0):
            res=res+i
if(x==res):
    print("Perfect No.")
else:
    print("Not Perfect")
        
