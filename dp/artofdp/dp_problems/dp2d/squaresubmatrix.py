def _square_sub_matrix(arr, i, j):
    if i == len(arr) or j == len(arr[0]):
        return 0
    if not arr[i][j]:
        return 0
    return 1 + min(_square_sub_matrix(arr, i + 1, j),
                   _square_sub_matrix(arr, i, j + 1),
                   _square_sub_matrix(arr, i + 1, j + 1))


def square_sub_matrix(arr):
    max_val = 0
    rows = len(arr)
    column = len(arr[0])

    for i in range(rows):
        for j in range(column):
            if arr[i][j]:
                max_val = max(max_val, _square_sub_matrix(arr, i, j))
    return max_val


def square_sub_matrix_bottom_up(arr):
    max_val = 0
    cache = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for i in range(len(cache)):
        for j in range(len(cache[0])):
            if i == 0 or j == 0:
                cache[i][j] = 1 if arr[i][j] else 0
            elif arr[i][j]:
                cache[i][j] = min(cache[i][j - 1],
                                  cache[i - 1][j],
                                  cache[i - 1][j - 1]) + 1
            if cache[i][j] > max_val:
                max_val = cache[i][j]

        return max_val+1


if __name__ == '__main__':
    arr = [
        [False, True, False, True],
        [True, True, True, True],
        [False, True, True, False]
    ]
    print(square_sub_matrix(arr))
    print(square_sub_matrix_bottom_up(arr))
