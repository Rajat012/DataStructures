
class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def print(self):
        if self.head==None:
            print("Linkedlist is Empty")
            return
        
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) +"-->"
            itr=itr.next
        print(llstr)    
    
    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        
        return count
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head==None:
            node=Node(data,self.head)
            self.head=node
        
        itr = self.head
        while itr.next:
            itr=itr.next
        node=Node(data,None)    
        itr.next = node 
    
    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        if index==0:
            insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next
    
    def remove_at(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    
    def insert_multiple(self,data_list):
            for data in data_list:
                self.insert_at_end(data)
    
    def insert_after_value(self,data_after,data):
        if self.head is None:
            return
        
        itr=self.head
        while itr:
            if(itr.data==data_after):
                node=Node(data,itr.next)
                itr.next=node
                return
            itr=itr.next
        raise Exception("Value Not Found")
    
    def remove_by_value(self,data):
        if self.head is None:
            return
        
        if self.head.data==data:
            self.head=self.head.next
            return
        
        itr=self.head
        while itr.next:
            if(itr.next.data==data):
                itr.next=itr.next.next
                break
            itr=itr.next
                
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(30)
    ll.insert_at_end(50)
    ll.insert_at(2,80)
    ll.insert_at(5,6)
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.insert_multiple([13,14,15,16,17,18])
    ll.print()
    print("length is :",ll.length())
    ll.insert_after_value(16,79)
    ll.print()
    print("length is :",ll.length())
    ll.remove_by_value(14)
    ll.print()
    print("length is :",ll.length())
    
    
        
