str1= input("")
count=0
str2=str1.lower()                                          # list1 = ["a","e","i","o","u"]
for x in str2:
    if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):    # if x in list1:
        count+=1
print (count)        
