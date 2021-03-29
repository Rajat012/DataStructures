
from collections import deque
class Stack:
    def __init__(self):
        self.stack= deque()
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def sizeof(self):
        return  len(self.stack)
    
    def isempty(self):
        return len(self.stack) == 0
    
    def reverseof(self,string):
        for i in string:
            self.push(i)
        str1=""
        for i in range(self.sizeof()):
            str1+=self.pop()
        return str1

def check_paran(string):
    s=Stack()
    dic={"}":"{","]":"[",")":"("}
    for i in string:
        if i==("(" or "[" or "{"):
            s.push(i)
        if i==(")" or "]" or "}"):
            if s.sizeof() == 0:
                return False
            
            if dic[i] == s.peek():
                s.pop()
    return s.isempty()
    
s=Stack()  
print(s.reverseof("We will conquere COVID-19"))
print(check_paran("({a+b})"))
print(check_paran("))((a+b}{"))
print(check_paran("((a+b))"))
print(check_paran("))"))
print(check_paran("[a+b]*(x+2y)*{gg+kk}"))

