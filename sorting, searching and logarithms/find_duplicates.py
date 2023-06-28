import unittest


def find_repeat(numbers):

    # Find a number that appears more than once
   
    floor = 1
    ceiling = len(numbers)-1
   
   
   
    while floor < ceiling:
       
       
        middlePoint = floor + (ceiling-floor)//2
       
       
       
        floor_number,mid_low_number = floor, middlePoint
       
        mid_up_number, ceiling_number = middlePoint+1,ceiling
       
       
        low_numbers = 0
        
        for i in numbers:
           
            if (i>=floor_number and i <= mid_low_number):
                low_numbers = low_numbers +1
                
        
        
            
            
        if low_numbers > (mid_low_number -floor_number +1):
            floor = floor_number
            ceiling = mid_low_number
            
        
        else:
            floor = mid_up_number
            ceiling = ceiling_number
         
        
        
    return floor
            














