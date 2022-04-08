def search_in_matrix(array, target):
    i = 0
    n = len(array[0])
    j = n-1
    while i < n-1 and j >= 0:
        if array[i][j] == target:
            return True
        elif array[i][j] < target:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':
    array = [
        [1, 2, 6, 7],
        [12, 13, 16, 21],
        [23, 25, 36, 48]
    ]
    # result = search_in_matrix(array, 36)
    # print(result)
    result = search_in_matrix(array, 349)
    print(result)

