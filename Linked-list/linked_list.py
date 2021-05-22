class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def InsertLast(self,value):
        newnode = Node(value)

        if self.start == None:
            self.start = newnode

        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
    
    def viewList(self):
        
        if self.start == None:
            print("no element present in list:")

        else:
            temp = self.start
            while temp:
                print(temp.data,end=" ")
                temp = temp.next

    def InsertMiddle(self,value):
        newnode = Node(value)
        
        if self.start == None:
            self.start = newnode

        else:
            slow_ptr = self.start
            fast_ptr = self.start

            while(fast_ptr != None and fast_ptr.next != None):
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            newnode.next = slow_ptr.next
            slow_ptr.next = newnode

        self.viewList()

    def printNthFromLast(self,value):
        temp = self.start

        length = 0
        while temp:
            temp = temp.next
            length +=1

        if value>length:
            print("Entered location is greater then the length.")

        else:
            temp = self.start
            for i in range(length-value):
                temp = temp.next
                print(temp.data)

    
l = LinkedList()
l.InsertLast(10)  
l.InsertLast(20)
l.InsertLast(30)
l.InsertLast(40)
l.InsertLast(50)
l.printNthFromLast(3)
#l.viewList()
#l.InsertMiddle(100)

