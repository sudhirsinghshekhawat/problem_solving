def valid_mountain(array):
    left = 0
    right = len(array) - 1
    n = len(array)
    while left < n-1 and array[left] < array[left + 1]:
        left += 1

    while right > 0 and array[right - 1] > array[right]:
        right -= 1

    if left > 0 and left == right and right < n-1:
        return True
    else:
        return False
