
def is_balanced(tree_root):

    # Determine if the tree is superbalanced

    
    nodesToVisit = [(tree_root,0)]
    depths = []
    
    i=0
    while len(nodesToVisit)>0:
        currentNode, depth = nodesToVisit.pop()
        
        
        if not currentNode.left and not currentNode.right:
            if depth not in depths:
                depths.append(depth)
            
            if (len(depths)>2 )or (len(depths)==2 and(abs(depths[0]-depths[1])>1)):
                return False
                
        
        else:
            
            if currentNode.left:
                nodesToVisit.append((currentNode.left, depth+1))
            if currentNode.right:
                nodesToVisit.append((currentNode.right, depth+1))
            
            
    
    return True
        