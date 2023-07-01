
def delete_node(node_to_delete):

    # Delete the input node from the linked list

    if node_to_delete.next == None:
        raise Exception("Can not delete last node with this technique")
    node_to_delete.value = node_to_delete.next.value
    node_to_delete.next = node_to_delete.next.next
    
    
    pass

