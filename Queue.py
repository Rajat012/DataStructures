
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

food_order_serve = Queue()

def place_order(orders):
    for order in orders:
        print("Placing order : ",order)
        food_order_serve.enqueue(order)
        time.sleep(1)

def serve_order():
    time.sleep(1)
    while True:
        order = food_order_serve.dequeue()
        print("Serving order : ",order)
        time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1=Thread(target=place_order(orders))
    t2=Thread(target=serve_order())
    t1.start()
    t2.start()

