from datastruct.classes.lists import LinkedList, Node

def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    result = LinkedList[int]()
    carry = 0
    
    current1, current2 = l1.head, l2.head
    tail = None
    
    while current1 or current2 or carry:
        val1 = current1.data if current1 else 0
        val2 = current2.data if current2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        new_node = Node(total % 10)
        
        if not result.head:
            result.head = new_node
        else:
            tail.next = new_node
        
        tail = new_node
        
        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next
    
    return result