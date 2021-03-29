
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def print_forward(self):
        if self.head==None:
            print("DoublyLinkedList is Empty")
            return
        
        itr=self.head
        dllstr=""
        while itr:
            dllstr+=str(itr.data)+ "-->"
            itr=itr.next
        print(dllstr)   
        
    def print_backward(self):
        if self.head==None:
            print("DoublyLinkedList is Empty")
            return
        
        last_node=self.get_last_node()
        itr=last_node
        dllstr=""
        while itr:
            dllstr+=itr.data+"-->"
            itr=itr.prev
        print(dllstr)
        
    def get_last_node(self):
        itr=self.head
        while itr:
            itr=itr.next
        return itr    
        
    def insert_at_beginning(self,data):
        if self.head==None:
            node=Node(data,self.head,None)
            self.head=node
            return
      
        node=Node(data,self.head,None)
        self.head.prev=node
        self.head=node
        
    def insert_at_end(self,data):
        if self.head==None:
            node=Node(data,None,None)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr = itr.next
        node=Node(data,None,itr)
        itr.next=node
    
    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        
        return count
    
    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next,itr)
                itr.next=node
                if node.next:
                    node.next.prev=node
                break    
            count+=1
            itr=itr.next
    
    def remove_at(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            self.head.prev=None
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                    break
            count+=1
            itr=itr.next
        
        
if __name__ == "__main__":
    dll=DoublyLinkedList()
    dll.insert_at_beginning(45)
    dll.insert_at_beginning(25)
    dll.insert_at_end(5)
    dll.insert_at_end(60)
    dll.insert_at_beginning(85)
    dll.insert_at_end(30)
    dll.insert_at_end(70)
    dll.print_forward()
    dll.print_backward()
    print("length is : ",dll.length())
    dll.insert_at(5,62)
    dll.insert_at(0,33)
    dll.insert_at(dll.length(),88)
    dll.print_forward()
    dll.print_backward()
    print("length is : ",dll.length())
    dll.remove_at(4)
    dll.remove_at(8)
    dll.remove_at(0)
    dll.insert_at_end(250)
    dll.print_forward()
    
    
    

   
