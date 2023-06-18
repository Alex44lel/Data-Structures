
def merge_lists (list_to_merge):
    list_to_return = []

    for sub_list in list_to_merge:
        list_to_return = merge_lists_helper(sub_list,list_to_return)

    print(list_to_return)


def merge_lists_helper(list1,list2):
    merged_list = []
    total_lenght = len(list1) + len(list2)
    merged_list_index = 0
    list_1_index = 0
    list_2_index = 0

    while merged_list_index < total_lenght:
        is_list1_index_ended = list_1_index >= len(list1)
        is_list2_index_ended = list_2_index >= len(list2)
        if(not is_list1_index_ended and (is_list2_index_ended or list1[list_1_index] < list2[list_2_index])):
            merged_list.append(list1[list_1_index])
            list_1_index +=1
        else:
            merged_list.append(list2[list_2_index])
            list_2_index +=1
        
        merged_list_index +=1

    return merged_list



merge_lists([[1,5,8,44],[2,3,10,12],[4,20,24,27],[9,13,15,23,34]])