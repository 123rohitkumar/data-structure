class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        
        if data<self.data:
            #left insert
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #right insert
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        #left traversal..
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements

    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        sum =0
        if self.left:
            sum = sum + self.left.calculate_sum()
        
        sum = sum+self.data

        if self.right:
            sum = sum + self.right.calculate_sum()
        
        return sum
    
    def delete(self,val):
        #leaf node
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:
            #no value
            if self.left is None and self.right is None:
                return None
            
            #one child
            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            max_value = self.left.find_max()
            self.left = max_value
            self.left = self.left.delete(max_value)
    
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0]) 
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ =='__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("sorted_list:",numbers_tree.in_order_traversal())
    print("min value in tree:",numbers_tree.find_min())
    print("max value in tree:",numbers_tree.find_max())
    print("Sum of tree:",numbers_tree.calculate_sum())
    print("after deleting the value:",numbers_tree.delete(20))
    

        



