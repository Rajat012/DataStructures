def binarySearch(list1,key):
  low=0
  high=len(list1)-1
  mid= (low+high)//2

  if (key>=list1[0] and key<=list1[high]):
    while True:
      while(key<list1[mid]):
        high=mid-1
        mid=(low+high)//2
      while(key>list1[mid]):
        low=mid+1
        mid=(low+high)//2
      if(key==list1[mid]):
        break
    return mid
  else:
    print("Key Not Found")
  
       
list1=[10,20,30,40,50,60,70]
ind=binarySearch(list1,10)
if (ind!=None):print(ind)
