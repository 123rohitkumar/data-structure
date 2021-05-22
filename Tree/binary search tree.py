
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return 
        
        #left side..
        if data <self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        #right side..
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        
        #visit left..
        if self.left:
            elements += self.left.in_order_traversal()

        #visit node..
        elements.append(self.data)

        #visit right..
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
        

    

    # def calculate_sum(self):
    #     left_sum = self.left.calculate_sum() if self.left else 0
    #     right_sum = self.right.calculate_sum() if self.right else 0
    #     return self.data + left_sum + right_sum
    
    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        
        sum += self.data

        if self.right:
            sum += self.right.calculate_sum() 
        
        return sum





    def delete(self):
        pass

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ =='__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(" sorted list:",numbers_tree.in_order_traversal())
    print("min value in tree:",numbers_tree.find_min())
    print("max value in tree:",numbers_tree.find_max())
    print("left sum:",numbers_tree.calculate_sum())








