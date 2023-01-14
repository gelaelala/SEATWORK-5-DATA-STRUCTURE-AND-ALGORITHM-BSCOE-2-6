# Create a demo using the letters in your fullname as the content of the binary tree

class BinarySearchTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child (self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child (data)
            else:
                self.left = BinarySearchTreeNode (data)
        else:
            if self.right:
                self.right.add_child (data)
            else:
                self.right = BinarySearchTreeNode (data)
    
    def in_order_traversal (self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append (self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal (self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append (self.data)

        return elements

    def pre_order_traversal (self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max (self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min (self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum (self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum

    def delete (self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            #min_val = self.right.find_min()
            #self.data = min_val
            #self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def search (self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree (elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters_tree = build_tree(["A", "N", "G", "E", "L", "A", "E", "C", "O", "R", "P", "U", "Z"])

    print ("In Order Traversal:", letters_tree.in_order_traversal())
    print ("Pre order Traversal:", letters_tree.pre_order_traversal())
    print ("Post Order Traversal:", letters_tree.post_order_traversal())
    print ("Maximum:", letters_tree.find_max())
    print ("Minimum:", letters_tree.find_min())

    #for searching a certain element
    
    print ("Is letter O present in the list? ", letters_tree.search('O'))
    print ("Is letter H present in the list? ", letters_tree.search('H'))

    #for deleting elements

    letters_tree = build_tree(["A", "N", "G", "E", "L", "A", "E", "C", "O", "R", "P", "U", "Z"])
    letters_tree.delete ('A')
    print ("After deleting the letter A:", letters_tree.in_order_traversal())

    letters_tree = build_tree(["A", "N", "G", "E", "L", "A", "E", "C", "O", "R", "P", "U", "Z"])
    letters_tree.delete ('Z')
    print ("After deleting the letter Z:", letters_tree.in_order_traversal())