#creating a class and for hash function..

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    #def add(self,key,val):
        #h = self.get_hash(key)
        #self.arr[h] = val

    #def get(self,key):
        #h =self.get_hash(key) 
        #return self.arr[h]
    
    def __getitem__(self,index):
        h =self.get_hash(index)
        return self.arr[h]

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h]=value


    

t = HashTable()
print(t.get_hash("march 6"))

t["march 6"]=120
t["march 9"]=130
t["march 10"]=140
t["march 17"]=150

print(t.arr)
print(t["march 6"])




