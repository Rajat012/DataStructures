'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expenses = [2200,2350,2600,2130,2190]
print(expenses)
# Q1
print("Extra Dollar Spent in Feb as compared to jan is : ",(expenses[1]-expenses[0]))
#Q2
first_quarter=expenses[0]+expenses[1]+expenses[2]
print("Total Expenses in First quarter is : ",first_quarter)
#Q3
for i in range(len(expenses)):
  if expenses[i]==2000:
    print("Month no. is : ",i)
    break
else:
  print("No Month Has Earned 2000$ " )
# or 2000 in expenses  
#Q4
expenses.append(1980)
print(expenses)
#Q5
expenses[3]=expenses[3]-200
print(expenses)


# 2nd Question
'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
'''

heros=['spider man','thor','hulk','iron man','captain america']
print(heros)
#Q1
print("length of the list is : ",len(heros))
#Q2
heros.append("black panther")
print(heros)
#Q3
heros.remove("black panther")
print(heros)
ind=heros.index("hulk")
heros.insert(ind,"black panther")
print(heros)
#Q4
heros[1:4]=["doctor strange",heros[2],"doctor strange"]
print(heros)
#Q5
heros.sort()
print(heros)

'''

# 3rd Question
'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
'''

max_num=int(input("Enter No. : "))
odd=[]
for i in range(1,max_num+1):
    if i%2==1:
        odd.append(i)
        
print(odd)        

'''
