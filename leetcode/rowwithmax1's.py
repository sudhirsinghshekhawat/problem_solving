def row_with_max_1s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    current_cols = cols - 1
    max_row_index = 0

    for i in range(rows):
        while current_cols >= 0 and matrix[i][current_cols] == 1:
            current_cols -= 1
            max_row_index = i

    return max_row_index


def row_with_max_0s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    current_cols = 0
    max_row_index = 0
    for i in range(rows):
        while current_cols < cols and matrix[i][current_cols] == 0:
            current_cols += 1
            max_row_index = i

    return max_row_index


matrix = [
    [1, 1, 0, 1],
    [1, 1, 1, 1, ]
    # [0, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 1, 1],
    # [0, 1, 1, 1, 1, 1],
]

print(row_with_max_1s(matrix))
# print(row_with_max_0s(matrix))
