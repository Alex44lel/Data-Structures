def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree
    
    nodes_to_visit=[(root,-float("inf"),float("inf"))]
    
        
    while(len(nodes_to_visit)>0):
        
        
        current_node, lower_bound,upper_bound = nodes_to_visit.pop()
        if current_node.value <= lower_bound or current_node.value >= upper_bound:
            return False
        
        if current_node.right:
            nodes_to_visit.append((current_node.right,current_node.value, upper_bound))
        if current_node.left:
            nodes_to_visit.append((current_node.left,lower_bound,current_node.value))

    return True
