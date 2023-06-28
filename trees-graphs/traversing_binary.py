
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert_left(self,value):
        self.left = Node(value)
        return self.left
    def insert_right(self,value):
        self.right = Node(value)
        return self.right

arbol = Node(2)
left = arbol.insert_left(3)
right = arbol.insert_right(4)
left.insert_left(30)
left.insert_right(33)
right.insert_left(40)
right.insert_right(44)


def depth_traversal_iterative(root):
    #we need a queue
    stack = [root]
    
    while len(stack)>0:
        current_node = stack.pop()
        
        print(current_node.value)
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
        
depth_traversal_iterative(arbol)
        

