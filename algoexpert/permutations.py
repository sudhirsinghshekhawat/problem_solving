def permutations_helper(i, perm_arr, arr):
    if i == len(arr) - 1:
        perm_arr.append(arr[:])
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            permutations_helper(i + 1, perm_arr, arr)
            arr[i], arr[j] = arr[j], arr[i]


def permutations(arr):
    perm_arr = []
    permutations_helper(0, perm_arr, arr)
    return perm_arr


if __name__ == '__main__':
    array = [1, 2, 3]
    result = permutations(array)
    print(result)

    string = "ABC"
    result = permutations(list(string))
    result = ["".join(ch) for ch in result]
    print(result)
