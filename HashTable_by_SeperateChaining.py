
class Hashtable:
    def __init__(self):
        self.Max=10
        self.arr=[[] for x in range(self.Max)]
   
    def hash_func(self,key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash%self.Max
    
    def __setitem__(self,key,value):
        hfunc=self.hash_func(key)
        for inx,item in enumerate(self.arr[hfunc]):
            if item[0] == key:
                self.arr[hfunc][inx] = (key,value)
                break
        else:
            self.arr[hfunc].append((key,value))
    
    def __getitem__(self,key):
        hfunc=self.hash_func(key)
        for item in self.arr[hfunc]:
            if item[0] == key:
                return item[1]
    
    def __delitem__(self,key):
        hfunc=self.hash_func(key)
        for inx,item in enumerate(self.arr[hfunc]):
            if item[0] == key:
                del self.arr[hfunc][inx]
            

if __name__== "__main__":
    h = Hashtable()
    h["march 6"] = 310
    h["march 7"] = 420
    h["march 8"] = 67
    h["march 17"] = 63457
    print(h.arr)
    h["march 17"] = 548
    print(h.arr)
    print(h["march 17"])
    del h["march 17"]
    print(h["march 6"])
    print(h.arr)
