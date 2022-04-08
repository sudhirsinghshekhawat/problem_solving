from queues.queue import Queue
from stacks.stack import Stack


# Todo : find the max sum in window

def reverse_queue_first_k_element(queue: Queue, k: int):
    stack1 = Stack()
    for i in range(k):
        stack1.push(queue.dequeue())

    while not stack1.is_empty():
        queue.enqueue(stack1.pop())

    for i in range(0, queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue


def reversal_queue(queue: Queue):
    stack1 = Stack()

    while not queue.is_empty():
        stack1.push(queue.dequeue())

    while not stack1.is_empty():
        queue.enqueue(stack1.pop())

    return queue


if __name__ == '__main__':
    queue = Queue()
    for i in range(11):
        queue.enqueue(i)

    print(queue)

    queue = reverse_queue_first_k_element(queue, 3)
    print(queue)

    reverse_queue = reversal_queue(queue)
    print(reverse_queue)
