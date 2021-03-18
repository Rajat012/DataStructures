no = int(input("Enter The No. : "))
if no>1:
    for i in range(2,no):
        if(no%i==0):
            print("Not Prime")
            break
    else:print("Prime No.")    
else:print("Enter No. Greater Than 1")
