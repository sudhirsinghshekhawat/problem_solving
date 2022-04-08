def print_matrix_rotation(arr):
    N = 4
    for j in range(N):
        for i in range(N - 1, - 1, -1):
            print(arr[i][j], end=' ')
        print()


def matrix_rotation(arr):
    N = 4
    # transpose of matrix
    for i in range(N):
        for j in range(i, N):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp

    # rotation of matrix
    for i in range(N):
        li = 0
        ri = len(arr[i]) - 1
        while li <= ri:
            temp = arr[i][li]
            arr[i][li] = arr[i][ri]
            arr[i][ri] = temp
            li = li + 1
            ri = ri - 1

    print(arr)


arr = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

# print(print_matrix_rotation(arr))
matrix_rotation(arr)
