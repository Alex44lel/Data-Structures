import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    if len(list_of_ints)<3:
        raise Exception("we need at least tree integers")
        
    highest_product_of_3 = list_of_ints[0]*list_of_ints[1]*list_of_ints[2]
    highest_product_of_2 = list_of_ints[0]*list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0]*list_of_ints[1]
    highest_num = max(list_of_ints[0],list_of_ints[1])
    lowest_num = min(list_of_ints[0],list_of_ints[1])
    
    
    for i in range(2,len(list_of_ints)):
        
        num =list_of_ints[i]
        highest_product_of_3 = max(highest_product_of_3,max(highest_product_of_2*num,lowest_product_of_2*num))
        highest_product_of_2= max(highest_product_of_2,num*highest_num,num*lowest_num)
        lowest_product_of_2 = min(lowest_product_of_2,num*lowest_num,num*highest_num)
        
        
        highest_num = max(num,highest_num)
            
        
        lowest_num =min(lowest_num,num) 
        
        print(i,list_of_ints[i], highest_product_of_2, lowest_product_of_2, lowest_num)
    return  highest_product_of_3