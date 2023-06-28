
def find_largest(node):
    current_node = node
    while current_node.right:
        current_node = current_node.right

    return current_node.value
    
def find_second_largest(root_node):
    if not root_node.right and not root_node.left:
    
        raise Exception("error")
    
    current =root_node
    while current:
        if current.left and not current.right:
            return find_largest(current.left)
            
        
        if current.right and not current.right.right and not current.right.left:
            return current.value
    
        current = current.right