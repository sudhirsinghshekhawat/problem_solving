class LRUCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maxsize = maxsize if maxsize else 1
        self.current_size = 0
        self.list_most_recent = DoublyLinkList()

    def insert_key_value_pair(self, key, value):
        if key not in self.cache:
            if self.current_size == self.maxsize:
                self.evict_least_recent()
            else:
                self.current_size += 1
            self.cache[key] = DoublyLinkList(key, value)
        else:
            self.replace_key(key, value)

        self.update_most_recent(self.cache[key])

    def evict_least_recent(self):
        key_to_remove = self.list_most_recent.tail.key
        self.list_most_recent.remove_tail()
        del self.cache[key_to_remove]

    def update_most_recent(self, node):
        self.list_most_recent.set_to_head(node)

    def replace_key(self, key, value):
        if key not in self.cache:
            raise Exception("the provided key not in cache")
        self.cache[key] = value

    def get_most_recent_key(self):
        if self.list_most_recent.head is None:
            return None
        return self.list_most_recent.head.key

    def get_value_from_key(self, key):
        if key not in self.cache:
            return None
        self.update_most_recent(self.cache[key])
        return self.cache[key].value


class DoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_to_head(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            node.next = self.head
            self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None


class DoublyLinkListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_bindings(self):
        if self.prev is not None:
            self.next.prev = self.prev
        if self.next is not None:
            self.prev.next = self.next
        self.prev = None
        self.next = None
