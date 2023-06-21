def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time

    counts = {}
    result = []
    for num in unsorted_scores:
        
        if(num in counts):
            counts[num]+= 1
        
        else:
            counts[num] = 1
            
        
    
    for i in range(highest_possible_score,-1,-1):
        
        if(i in counts):
            for j in range(0,counts[i]):
                result.append(i)
                
    return result
