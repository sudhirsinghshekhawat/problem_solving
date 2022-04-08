from linklist import linkedlist_operation
from linklist.singlylinklist import Node


def remove_duplicate_from_list(head):
    """removing the duplicate from link list"""
    data_set = set()
    prev = None

    start = head
    while start:
        if start.data not in data_set:
            data_set.add(start.data)
            # data_set[start.data] = None
            prev = start
        else:
            prev.next = start.next
        start = start.next


def sum_of_element():
    """
    Sum of elements using link list
    """

    linklist1 = linkedlist_operation.create_linklist()
    linklist2 = linkedlist_operation.create_linklist()
    linklist1.head.data = 8
    linklist2.head.data = 8

    reverse_linklist1 = linkedlist_operation.reverse_linklist(linklist1.head)
    reverse_linklist2 = linkedlist_operation.reverse_linklist(linklist2.head)

    start1 = reverse_linklist1
    start2 = reverse_linklist2
    carry = 0

    while start1 or start2:
        sum = start1.data + start2.data + carry
        carry = 0

        if sum // 10 > 0:
            carry = sum // 10
        if start1.next:
            print(sum % 10, end='')
        else:
            print(sum, end='')

        start1 = start1.next
        start2 = start2.next


if __name__ == '__main__':
    linklist = linkedlist_operation.create_linklist();
    linklist.insert_at_end(Node(1, None))
    linklist.print_linklist()
    remove_duplicate_from_list(linklist.head)
    linklist.print_linklist()
    sum_of_element()
