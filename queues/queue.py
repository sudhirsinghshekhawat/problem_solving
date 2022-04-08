class Queue:

    def __init__(self) -> None:
        self.items = []  # type:ignore

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'queue : {self.items}'


if __name__ == '__main__':
    q = Queue()
    print(f'q size : {q.size()}')
    print(f'q is empty : {q.is_empty()}')
    print(q.dequeue())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(13)
    print(q)
    print(q.dequeue())
    print(q)

