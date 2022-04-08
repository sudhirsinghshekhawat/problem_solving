"""
 This module for the operations of link list
"""

from linklist.singlylinklist import LinkList, Node


def reverse_linklist(head):
    """ function for reversing the link list"""
    current = head
    prev = None

    while current:
        _next = current.next
        current.next = prev
        prev = current
        current = _next

    return prev


def middle_element_linklist(head):
    """function to find middle element of link list """
    if not head:
        return None
    slow_ptr = head
    fast_ptr = head

    while slow_ptr and fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


def nth_node_from_end(head, n):
    if not head:
        return None

    start = head
    current = head

    i = 0
    while i < n:
        if start:
            start = start.next
            i = i + 1
        else:
            return None
    while start:
        current = current.next
        start = start.next
    return current


def reverse_k_element_from_last(head, k):
    kth_element = nth_node_from_end(head, k)
    print(f'kth element : {kth_element}')

    if kth_element:
        reverse = reverse_linklist(kth_element)
        print(f'reverse : {reverse}')

    start = head
    while start.next != reverse.next:
        start = start.next
    start.next = reverse


def create_linklist():
    """function for creating the link list"""
    _linklist = LinkList()
    for i in range(1, 6):
        _linklist.insert_at_end(Node(i, None))
    _linklist.print_linklist()
    return _linklist


def linklist_length_even_odd(head):
    if not head:
        return 'N/A'
    start = head
    while start and start.next:
        start = start.next.next

    return 'Odd' if start else 'Even'


if __name__ == '__main__':
    linklist = create_linklist()
    linklist.head = reverse_linklist(linklist.head)
    print('reversed linklist')
    linklist.print_linklist()

    middle_element = middle_element_linklist(linklist.head)
    print(f'middle element : {middle_element}')

    nth_node = nth_node_from_end(linklist.head, 3)
    print(f'2rd node from end : {nth_node}')

    reverse_k_element_from_last(linklist.head, 2)
    linklist.print_linklist()

    print(f'length of linklist is : {linklist_length_even_odd(linklist.head)}')
