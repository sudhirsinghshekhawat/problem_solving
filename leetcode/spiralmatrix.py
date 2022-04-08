def spiral_matrix(arr, rows, cols):
    i = k = l = 0
    last_row = rows - 1
    last_col = cols - 1
    result = []

    while k <= last_row and l <= last_col:
        for i in range(l, last_col + 1):
            result.append(arr[k][i])
        k += 1

        for i in range(k, last_row + 1):
            result.append(arr[i][last_col])
        last_col -= 1

        if k <= last_row:
            for i in range(last_row, l - 1, -1):
                result.append(arr[last_row][i])
        last_row -= 1

        if l <= last_col:
            for i in range(last_row, k - 1, -1):
                result.append(arr[i][l])
        l += 1

    return result

    # i = k = l = 0
    # last_row = rows - 1
    # last_col = cols - 1
    # result = []
    # while k <= last_row and l <= last_col:
    #     for i in range(l, last_col + 1):
    #         result.append(arr[k][i])
    #     k += 1
    #
    #     for i in range(k, last_row + 1):
    #         result.append(arr[i][last_col])
    #     last_col -= 1
    #
    #     if k <= last_row:
    #         for i in range(last_col, l-1, -1):
    #             result.append(arr[last_row][i])
    #     last_row -= 1
    #
    #     if l <= last_col:
    #         for i in range(last_row, k-1, -1):
    #             result.append(arr[i][l])
    #     l += 1
    #
    # return result


arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

result = spiral_matrix(arr, 4, 5)
print(result)
