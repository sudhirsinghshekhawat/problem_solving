class Node:
    def __init__(self, elements):
        self.next = None
        self.elements = elements
        self.num_of_elements = len(self.elements)


# [] -->     [] --> [] -->[] --> None
# 0 - 'a'    4-'d'        5--'e'
# 1 - 'b'                 6--'f'
# 2 - 'c'
# find(head,pos)

def find(head, pos):
    if not head:
        return None
    current = head
    count = 0

    while current:
        if count + current.num_of_elements > pos:
            return current.elements[pos - count]
        count += current.num_of_elements
        current = current.next
    return None


if __name__ == '__main__':
    node1 = Node(['a', 'b', 'c'])
    node2 = Node(['d'])
    node3 = Node([])
    node4 = Node(['e', 'f'])
    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(find(head, 0))
    print(find(head, 1))
    print(find(head, 2))
    print(find(head, 3))
    print(find(head, 4))
    print(find(head, 5))
    print(find(head, 6))
    print(find(head, 7))
