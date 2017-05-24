"""
Implement quadratic probing as a rehash technique.
"""

class quadroProbing:
    def __init__(self):
         self.size = 11
         self.data = [None] * self.size

    def put(self,key):
        slot = key%self.size
        if self.data[slot] == None:
            self.data[slot] = key
        else:
            i = 0
            while self.data[slot] != None:
                i += 1
                print i, i**2
                slot = (slot+i**2)%11
            self.data[slot] = key

    def __str__(self):
        return str(self.data)


ds = quadroProbing()
ds.put(54)
ds.put(26)        
ds.put(93)
ds.put(17)
ds.put(77)
ds.put(31)

print ds

ds.put(44)
print ds
ds.put(55)
print ds
ds.put(20)
print ds

