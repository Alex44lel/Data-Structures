def max_duffel_bag_value(cake_tuples, weight_capacity):

    # Calculate the maximum value we can carry
   
    max_value_for_each_weight = [0]*(weight_capacity+1)
    
    for i in range(0,weight_capacity+1):
        
        for weight,value in cake_tuples:
            if value != 0:
                if weight == 0:
                    return float('inf')

                
                if weight <= i :
                    max_value_for_each_weight[i] = max(max_value_for_each_weight[i],value + max_value_for_each_weight[i-weight])
        
     

    return max_value_for_each_weight[weight_capacity]