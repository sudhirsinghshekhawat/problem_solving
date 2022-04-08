"""
You are given an array of positive integers, find the subarray containing unique elements with maximum sum and print the sum.

4,3,2,7,8,2,3,5

Output - 25
"""


def unique_subarray_sum(array):
    i = 0
    j = 1
    visited = {}
    current_sum = array[0]
    max_sum = current_sum
    visited[array[0]] = 1

    while j < len(array) and i < len(array) - 1:
        if array[j] not in visited:
            current_sum += array[j]
            max_sum = max(current_sum, max_sum)
            visited[array[j]] = 1
            j += 1
        else:
            current_sum -= array[i]
            del visited[array[i]]
            i += 1

    return max_sum


arr = [4, 3, 2, 7, 8, 2, 3, 5]
result = unique_subarray_sum(arr)
print(result)
