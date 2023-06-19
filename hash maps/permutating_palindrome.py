#my approach
def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    word = {}
    for i in the_string:
        if(i not in word):
            word[i] = 1
        else:
            word[i] += 1
            
    
    odd_counts = 0
    
    for value in word.values():
        if(value%2!=0):
            odd_counts +=1
        
        if odd_counts >1:
            return False

    return True


#cleaner approach

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pai