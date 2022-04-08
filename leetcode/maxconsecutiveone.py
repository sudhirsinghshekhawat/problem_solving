def max_consecutive_one(arr):
    current_count = 0
    max_count = 0

    for val in arr:
        if val == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count


arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
result = max_consecutive_one(arr)
print(result)
