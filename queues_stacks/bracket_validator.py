def is_valid(code):

    # Determine if the input code is valid
    stack = []
   
    
    
    for i in code:
        if i =="(" or i =="[" or i =="{":
            stack.append(i)
        
        if i==")":
            if (len(stack) ==0 or stack.pop()!="("):
                return False
        
        if i=="]":
            if (len(stack) ==0 or  stack.pop()!="["):
                return False
                
        if i=="}":
            if (len(stack) ==0 or  stack.pop()!="{"):
                return False
                
    
    if len(stack)>0:
        return False
    return True