import unittest


def find_rotation_point(words):

    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
       
        mid = floor_index+((ceiling_index-floor_index)//2)
        
        
        if (floor_index + 1 == ceiling_index):
            return ceiling_index 
            
        if words[mid] >= first_word:
            floor_index = mid 
        
        
        else :
            ceiling_index = mid 
        
        
        
            
    return -1





