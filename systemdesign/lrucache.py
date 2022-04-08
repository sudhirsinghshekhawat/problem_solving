class Node:

    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = dict()
        self.head = Node('#', 0)
        self.tail = Node('_', 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        next_node = self.head.next
        previous_node = self.head

        previous_node.next = node
        next_node.prev = node

        node.next = next_node
        node.prev = previous_node

    def _remove(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def get(self, key):
        if key in self.hashMap:
            node = self.hashMap[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.hashMap:
            self._remove(self.hashMap[key])
        new_node = Node(key, value)
        self._add(new_node)
        self.hashMap[key] = new_node

        if len(self.hashMap) > self.capacity:
            node_to_remove = self.tail.prev
            self._remove(node_to_remove)
            del self.hashMap[node_to_remove.key]
            
