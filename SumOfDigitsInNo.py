x=int(input(" Enter No. : "))
total=0
length=len(str(x))

while(x>0):                    #for i in range(length):
    rem=x%10
    x=x//10
    total+=rem
    

print(total) 
#print(x)
