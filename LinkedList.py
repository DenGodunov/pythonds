"""
"""

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def setNext(self, item):
        self.next = item

    def setData(self, item):
        self.data = item

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
        

class UnorderedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.head==None:
            self.lastNode = temp
        self.head = temp
        self.size += 1
            

    def size(self):
        return self.size

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        
        else:
            previous.setNext(current.getNext())

        self.size -= 1

    def __str__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.data)
            node = node.next
            while node:
                result += ", " + str(node.data)
                node = node.next
        result += "]"
        return result 

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.lastNode = temp
        else:
            self.lastNode.setNext(temp)
            self.lastNode = temp
        self.size += 1
        



new_list = UnorderedList()
new_list.add(5)
new_list.add(43)


