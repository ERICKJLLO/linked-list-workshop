from datastruct.classes.lists import LinkedList, Node

def sort_list_by_insertion(linked_list: LinkedList[int]) -> LinkedList[int]:
    if linked_list.is_empty() or linked_list.head.next is None:
        return linked_list
    
    sorted_list = LinkedList[int]()
    current = linked_list.head
    
    while current:
        next_node = current.next
        
        if sorted_list.is_empty() or sorted_list.head.data >= current.data:
            current.next = sorted_list.head
            sorted_list.head = current
        else:
            temp = sorted_list.head
            while temp.next and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        
        current = next_node
    
    return sorted_list
