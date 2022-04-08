def max_area(arr):
    max_area = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            curr_area = (j - i) * min(arr[i], arr[j])
            max_area = max(max_area, curr_area)
    return max_area


def max_area1(arr):
    max_area = 0
    i = 0
    j = len(arr) - 1
    while i < j:
        curr_area = (j - i) * min(arr[i], arr[j])
        max_area = max(max_area, curr_area)
        if arr[i] < arr[j]:
            i = i + 1
        else:
            j = j - 1
    return max_area


arr = [1, 5, 6, 3, 4, 2]

print(max_area(arr))
print(max_area1(arr))
