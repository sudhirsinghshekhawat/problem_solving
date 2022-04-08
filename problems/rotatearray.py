arr = [1, 2, -1, 3, -1, 2, 4, 5, 6]


def rotate_array(arr, k):
    arr = arr[k:] + arr[:k]
    return arr


result = rotate_array(arr, 3)
print(result)

result = rotate_array(arr, 2)
print(result)

result = rotate_array(arr, 4)
print(result)
