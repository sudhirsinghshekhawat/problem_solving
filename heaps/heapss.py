from heaps.exceptions import Empty


class PriorityQueueBase:
    """" Abstract base class for priority queue """

    class _item:
        """ Light weight composite to store 
        priority queue items """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def is_empty(self):
            return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self) -> None:
        self._data = []

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _has_left(self, i):
        return self._left(i) < len(self)

    def _has_right(self, i):
        return self._right(i) < len(self)

    def _swap(self, i, j):
        """ swap the element of array i and j """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        small_child = 0
        right = 0
        if self._has_left(j):
            left = self._left(j)
            small_child = left
        if self._has_right(j):
            right = self._right(j)
        if small_child > right:
            small_child = right
        if self._data[small_child] < self._data[j]:
            self._swap(small_child, j)
            self._downheap(small_child)

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append((key, value))
        self._upheap(len(self) - 1)

    def min(self):
        if self.is_empty():
            raise Empty("Heap is empty")
        item = self._data[0]
        return (item._key, item._val)

    def remove_min(self):
        if self.is_empty():
            raise Empty("Heap is empty")
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._val)
