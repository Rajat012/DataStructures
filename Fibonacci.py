x = int(input("Enter Total Elements"))
a=0
b=1
if(x>1):
    print(a,b,end=" ")
    for i in range(2,x):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
else:print(a)        
