class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def InsertLast(self,value):
        NewNode = Node(value)

        if self.start == None:
            self.start = NewNode

        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = NewNode

    def printMiddel(self):
        fast_ptr = self.start
        slow_ptr = self.start
        
        if self.start !=None:
            while (fast_ptr != None and fast_ptr.next != None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is:",slow_ptr.data)

    
    def viewList(self):

        if self.start == None:
            print("list is empty:")

        else:
            temp = self.start
            while temp:
                print(temp.data,end=' ')
                temp = temp.next

    def deleteFirst(self):
        if self.start ==None:
            print("list is empty:")
        else:
            self.start = self.start.next

    def deletemiddle(self):
        #first i need to know the miidle then i can remove it .
        fast_ptr = self.start
        slow_ptr = self.start
        prev = None

        if self.start !=None:
            while (fast_ptr != None and fast_ptr.next != None):
                fast_ptr = fast_ptr.next.next
                prev = slow_ptr
                slow_ptr = slow_ptr.next
            prev.next = slow_ptr.next
            print("After removing the middle linled list is:",self.viewList())


l = LinkedList()
l.InsertLast(10)
l.InsertLast(20)
l.InsertLast(30)
l.InsertLast(40)
l.InsertLast(50)
#l.InsertLast(60)
# #l.deleteFirst()
# l.viewList()
# print()
# l.printMiddel()
l.deletemiddle()