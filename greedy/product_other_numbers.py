import unittest

def get_products_of_all_ints_except_at_index(int_list):
    
    if len(int_list)<=1:
        raise Exception("Need more than one input")
    # Make a list with the products
    result=[]
    products_after= []
  
    for i,num in enumerate(int_list):
        if(i==0): result.append(1)
        
        else:
            result.append(int_list[i-1]*result[i-1])


    print(result)
    reversed_lenght = len(int_list)*-1
    j=-1
    i= 0
    mult=1
    while j>=reversed_lenght:
        
        if(j==-1): result[j]= result[j]*mult
        
        else:
            mult = mult * int_list[j+1]
            result[j]= result[j]*mult
        j-=1 
        i+=1
      
    
    return result