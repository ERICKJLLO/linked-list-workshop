from datastruct.classes.lists import LinkedList, Node

def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:
    if linked_list.is_empty() or linked_list.head.next is None:
        return linked_list
    
    dummy = Node(0)
    dummy.next = linked_list.head
    prev, current = dummy, linked_list.head
    
    while current and current.next:
        next_pair = current.next.next
        second = current.next
        
        second.next = current
        current.next = next_pair
        prev.next = second
        
        prev = current
        current = next_pair
    
    linked_list.head = dummy.next
    return linked_list
