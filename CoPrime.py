num1=int(input("Enter no's : "))
num2=int(input("Enter no's : "))

divisors=[]
count=0
for i in range(2,num1+1):
  if(num1%i==0):
    divisors.append(i)
for i in range(2,num2+1):
  if(num2%i==0):
    if i in divisors:
      count+=1

if(count==0):
  print("Co-Prime Numbers")
else:
  print("Not Co-Prime")

# Using gcd function of fractions module 
'''
from fractions import gcd  
num1=int(input("Enter no's : "))
num2=int(input("Enter no's : "))
if gcd(num1,num2)==1:
  print("Coprime")
else:print("Not Coprime")  
'''
