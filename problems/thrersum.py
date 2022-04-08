def three_sum(arr):
    arr.sort()
    for i in range(len(arr) - 3):
        left = i + 1
        right = len(arr) - 1


