x  = int(input("Entr No. of Rows : "))
count=0
for row in range(x):
    for col in range(x):
        if(col<=row):
            count+= 1
            print(count,end=" ")
        else:
            print(" ",end=" ")
    print()        
    

# cccc
x= int(input("Enter NO. of Rows : "))
cen=x//2
for rows in range(cen+1):
    for cols in range(x):
        if(rows==cen or cols==(cen-rows) or cols==(cen+rows)):
            print("*",end="")
        else:
            print(" ",end="")
    print()    
    

# center triangle
x= int(input("Enter NO. of Rows : "))
for rows in range(x):
    for cols in range((2*x)-1):
        if(rows==x-1 or cols==(x-rows) or cols==(x+rows)):
            print("*",end="")
        else:
            print(" ",end="")
    print()        

    
