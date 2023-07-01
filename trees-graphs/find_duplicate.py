
def find_duplicate(int_list):

    # Find a number that appears more than once ... in O(n) time
    
    n= len(int_list)-1
    
    current_pos = len(int_list)
    #traverse the list n positions to be in a loop
    
    for _ in range(n):
        current_pos = int_list[current_pos-1]
    
    #no we are in the loop
    #traverse loop until finding start point and get loop lenght
   
    start_pos = current_pos
    current_pos = int_list[current_pos-1]
    loop_lenght=1
    while start_pos != current_pos:
        current_pos = int_list[current_pos-1]
        loop_lenght+=1


    #start over with two pointes
    current_pos = len(int_list)
    current_pos_lenght = int_list[current_pos-1]
    current_pos = int_list[current_pos-1]
    
    
    for _ in range(loop_lenght):
        current_pos_lenght=int_list[current_pos_lenght-1]
    
    while current_pos != current_pos_lenght:
        current_pos = int_list[current_pos-1]
        current_pos_lenght = int_list[current_pos_lenght-1]
    
    return current_pos

