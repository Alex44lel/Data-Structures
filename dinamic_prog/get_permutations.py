def get_permutations(string):
    # Generate all permutations of the input string
    
    #base case
    
    if len(string)<=1:
        return set([string])
        
    all_chars_except_last = string[:-1]
    
    last_char = string[-1]
    
    
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
        
    
    permutations = set()
    
    
    for permutation in permutations_of_all_chars_except_last:
        for pos in range((len(permutation)+1)):
            
            newWord = (permutation[:pos] + last_char + permutation[pos:])
            permutations.add(newWord)

    return permutations


print(get_permutations("oso"))