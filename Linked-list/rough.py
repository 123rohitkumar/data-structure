class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insertLast(self,val):
        newnode = node(val)

        if self.start == None:
            self.start = newnode

        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = newnode

    def viewList(self):
        if self.start ==None:
            print("linked list is empty:")

        else:
            temp = self.start
            while temp:
                print(temp.data,end =" ")
                temp = temp.next

    def InsertMiddle(self,value):
        newnode = node(value)

        if self.start == None:
            self.start = newnode
        
        else:
            slow_ptr = self.start
            fast_ptr = self.start

            while(fast_ptr!=None and fast_ptr.next!=None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            
            newnode.next = slow_ptr.next
            slow_ptr.next = newnode
        
        self.viewList()

    def printNthFromLast(self,value):
        length = 0
        temp = self.start
        while temp:
            length +=1
            temp = temp.next
        print(length)

        if value>length:
            print("Entered location is greater then length:")

        else:
            temp = self.start
            for i in range(length-value):
                temp = temp.next
            print(temp.data) 





l = LinkedList()
l.insertLast(10)
l.insertLast(20)
l.insertLast(30)
l.insertLast(40)
l.insertLast(50)
l.InsertMiddle(100)
l.printNthFromLast(4)
#l.viewList()


