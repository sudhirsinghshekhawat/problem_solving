import heapq

if __name__ == '__main__':
    q = []
    q.append((1, 'sudhir'))
    q.append((3, 'Bhuvik'))
    q.append((2, 'Pinki'))

    q.sort(reverse=True)
    print(q)

    q1 = [] # type:ignore
    heapq.heappush(q1, (2, 'code'))
    heapq.heappush(q1, (1, 'eat'))
    heapq.heappush(q1, (3, 'sleep'), )

    arr = [12, 1, 3, 4, 5, 6, 7]
    q1 = []
    heapq.heappush(q1, 12)
    heapq.heappush(q1, 1)
    heapq.heappush(q1, 3)

    i = 3
    while i < len(arr):
        print(heapq.heappushpop(q1, arr[i]))
        i = i + 1
