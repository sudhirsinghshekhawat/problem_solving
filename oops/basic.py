import heapq
from queue import PriorityQueue

arr = [12, 11, 8, 7]
q = PriorityQueue(arr)

heapq.heapify(arr)
# q.put(11)
# q.put(8)
# q.put(6)

while not q.empty():
    print(q.get())

