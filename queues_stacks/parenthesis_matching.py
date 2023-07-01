
def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    
    
    oppened=0
    for i in range(opening_paren_index,len(sentence)):
        
        if sentence[i] == "(":
         
            oppened +=1
           
            
        if sentence[i] == ")":
            oppened -=1
            
            if (oppened == 0):
                return i
    
            
    raise Exception("No closing parenthesis :(") 
   

    return -1
