class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def reverse_linklist(head):
    current_node, prev_node = head, None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node
