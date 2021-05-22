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
        if self.start==None:
            print("Linked list is empty..")

        else:
            temp = self.start
            while temp:
                print(temp.data,end=" ")
                temp = temp.next

    def InsertMiddle(self,value):
        newnode = Node(value)

        if self.start == None:
            self.next = newnode

        else:
            slow_ptr = self.start
            fast_ptr = self.start

            while(fast_ptr !=None and fast_ptr.next != None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next

            newnode.next = slow_ptr.next
            slow_ptr.next = newnode

        self.viewList()

    def printNthFromLast(self,value):
        temp = self.start
        length = 0
        while temp:
            temp = temp.next
            length +=1
        print(length)

        if value>length:
            print("Enterd location  is greater then length..")
            return
        
        else:
            temp = self.start
            for i in range(length-value):
                temp = temp.next
            print(temp.data)  

    

    def detectLoop(self):
        fast_ptr = self.start
        slow_ptr = self.start
        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if (slow_ptr == fast_ptr):
                return 
 

l = LinkedList()
l.InsertLast(10)
l.InsertLast(20)
l.InsertLast(30)
l.InsertLast(40)

l.InsertMiddle(100)
#l.printNthFromLast(3)
#create a loop for testing..
l.start.next.next.next.next = l.start
if(l.detectLoop()):
    print("Found Loop")
else:
    print("No Loop")


        












