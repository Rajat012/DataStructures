
from collections import deque
from threading import *
import time

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()
    
    def sizeof(self):
        return len(self.queue)
    
    def isempty(self):
        return len(self.queue)==0
    
    def print(self):
        for i in range(len(self.queue)):
            print(self.queue[i])
    
if __name__ == "__main__":
    binary__queue = Queue()
    for i in range(1,11):
        x = bin(i)
        binary__queue.enqueue(x)
    print(binary__queue.queue)
    print(binary__queue.queue[-1])
    binary__queue.print()
    
    for i in range(len(binary__queue.queue)):
        x=binary__queue.dequeue().split("b")
        print(x[1])

