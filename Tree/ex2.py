#binary tree
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data 
        self.right=None
        self.left=None

    def add_child(self,data):
        if data ==self.data:
            return
        
        if data < self.data:
            #add data to left subtree:
            if self.left:
                #you are not in leaf node:
                self.left.add_child(data)
            else:
                #now you are on leaf node:
                self.left =BinarySearchTreeNode(data)

        else:
            #add data to right subtre:
            if self.right:
                self.right.add_child(data)

            else:
                self.right =BinarySearchTreeNode(data)
    
    #search the value:
    def search(self,value):
        if self.data == value:
            return True
           
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False




    
    #print the tree element:
    def in_order_traversal(self):
        elements=[]
        
        #visit left tree:
        if self.left:
            elements += self.left.in_order_traversal()
        
        #visit base node
        elements.append(self.data)

        #visit right tree:
        if self.right:
            elements += self.right.in_order_traversal()   
        
        return elements

    #for finding the max and minimum valus in tree:
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    #delete functionality:
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left =self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right =self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            #min_val = self.right.find_min()
            #self.data = min_val
            #self.right=self.right.delete(min_val)

            max_val = self.left.find_max()
            self.left =max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    print("printing tree with these elements:",elements)
        
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print("after deleting value from tree:",numbers_tree.in_order_traversal())

    
        
     