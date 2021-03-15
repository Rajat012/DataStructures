def noOfRows(x):
    for i in range(1,x+1):
        for j in range (i):
            print(j+1,end=" ")
        print("")
        
a=int(input("Enter No. of Rows  :  "))
noOfRows(a)

# Hollow Right angle Triangle 
def noOfRows(x):
    for i in range(1,x+1):
        for j in range (i):
            if(j==0 or j==i-1 or i==x):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
        
a=int(input("Enter No. of Rows  :  "))
noOfRows(a)

#Hollow Triangle Method 2
x = int(input("Enter No. of Rows : "))

for row in range(x):
    for col in range(x):
        if(col==0 or row==x-1 or col==row):
            print("*",end="")
        else:
            print(" ",end="")
    print()        

# hollow up-down r ang Triangle
x  = int(input("Entr No. of Rows : "))

for row in range(x):
    for col in range(x):
        if(col==x-1 or row==0 or row==col):
            print("*",end="")
        else:
            print(" ",end="")
    print()        

# up-down r angle Triangle
x  = int(input("Entr No. of Rows : "))

for row in range(x):
    for col in range(x):
        if(col>=row):
            print("*",end="")
        else:
            print(" ",end="")
    print(" "*row)        
    

# Using While Loop
x= int(input("Enter NO. : "))
rows=1
while(rows<=x):
    cols=1
    while(cols<=rows):
        print("*",end="")
        cols+=1
    print()
    rows+=1


