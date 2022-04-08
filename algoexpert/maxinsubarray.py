def max_in_subarray(arr):
    max_sum = arr[0]
    max_so_far = arr[0]
    for i in range(1, len(arr)):
        max_so_far = max(max_so_far + arr[i], arr[i])
        max_sum = max(max_sum, max_so_far)
    return max_sum


arr = [1, 2, 3, -2, 5]
result = max_in_subarray(arr)
print(result)


print("hello")
