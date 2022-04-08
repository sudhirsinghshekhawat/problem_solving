def check_sum(arr, total):
    number_set = {}
    for i in arr:
        diff = total - i
        if number_set.get(diff, False):
            return True
        number_set[i] = True
    return False


arr = [1, 2, 3, 4, 5, 6, 7]
print(check_sum(arr, 5))
print(check_sum(arr, 10))
print(check_sum(arr, 11))
print(check_sum(arr, 12))
print(check_sum(arr, 15))
print(check_sum(arr, 6))
