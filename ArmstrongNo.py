# Taking input as a String 
x= input("Enter No.")
a=len(x)
res=0
for i in range(0,a):
    q=int(x[i])
    expo=q**a
    res=res+expo
if(int(x)==res):
    print("Armstrong No.")
else:
    print("Not an Armstrong No.")
    
    
# method 2 Taking input in Integer Form
x= int(input("Enter No."))
a=len(str(x))
res=0
num=x
while(num!=0):
    rem=num%10
    expo=rem**a
    res=res+expo
    num=num//10
if(x==res):
    print("Armstrong No.")
else:
    print("Not an Armstrong No.")

    
