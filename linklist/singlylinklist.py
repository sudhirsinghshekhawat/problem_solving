class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def __str__(self):
        return f'data : {self.data} , next: {self.next.data}'


class LinkList:
    head: Node = None # type: ignore
    length: int = 0

    def linklist_length(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def insert_at_beginning(self, node: Node):
        node.set_next(self.head)
        self.head = node
        self.length = self.length + 1

    def print_linklist(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.get_next()
        print()

    def insert_at_end(self, node):

        self.length = self.length + 1
        if self.head is None:
            self.head = node
            return

        if self.head is not None:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(node)
            return

    def insert_at_position(self, node, pos):
        if pos < 0 or pos > self.length:
            print(f'please enter the pos between 0 and {self.length}')
            return

        if pos == 0:
            self.insert_at_beginning(node)
            return

        if pos == self.length:
            self.insert_at_end(node)
            return

        current = self.head
        count = 1

        while count < pos - 1:
            count = count + 1
            current = current.get_next()
        node.set_next(current.get_next())
        current.set_next(node)
        self.length = self.length + 1

    def delete_first_node(self):
        if self.length == 0:
            print(f'link list is empty')
            return
        self.head = self.head.get_next()
        self.length = self.length - 1

    def delete_last_node(self):
        if self.length == 0:
            print(f'link list is empty')
            return
        current = self.head
        previous = self.head
        while current.get_next():
            previous = current
            current = current.next

        previous.set_next(None)
        self.length = self.length - 1

    def delete_link_list(self):
        self.head = None
        self.length = 0


if __name__ == '__main__':
    linklist = LinkList()
    length_of_list = linklist.linklist_length()
    print(f'length of linklist : {length_of_list}')
    node = Node(1, None)
    linklist.insert_at_beginning(node)
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    node = Node(2, None)
    linklist.insert_at_beginning(node)
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    node = Node(3, None)
    linklist.insert_at_end(node)
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    node = Node(4, None)
    linklist.insert_at_end(node)
    node = Node(5, None)
    linklist.insert_at_end(node)
    linklist.print_linklist()
    node = Node(33, None)
    linklist.insert_at_position(node, 4)
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    node = Node(66, None)
    linklist.insert_at_position(node, 6)
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    node = Node(11, None)
    linklist.insert_at_position(node, 0)
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    linklist.delete_first_node()
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    linklist.delete_first_node()
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    linklist.delete_last_node()
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    linklist.delete_last_node()
    linklist.print_linklist()
    print(f'length of linklist : {linklist.length}')
    linklist.delete_link_list()
    print(f'length of linklist : {linklist.length}')
