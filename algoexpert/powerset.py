# time complexity = O(n*2^n)
# space complexity = O(n*2^n)
# Iterative solution
def power_set(arr):
    subset = [[]]
    for element in arr:
        for i in range(len(subset)):
            current_subset = subset[i]
            subset.append(current_subset + [element])
    return subset


# recursive solution
def power_set_1(arr, idx=None):
    if idx is None:
        idx = len(arr) - 1
    if idx < 0:
        return [[]]
    ele = arr[idx]
    subset = power_set_1(arr, idx - 1)
    for i in range(len(subset)):
        cur_subset = subset[i]
        subset.append(cur_subset + [ele])
    return subset


if __name__ == '__main__':
    array = [1, 2, 3]
    power_sets = power_set(array)
    print(power_sets)

    power_sets = power_set_1(array)
    print(power_sets)
