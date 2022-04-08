def minimum_passes_matrix(matrix):
    passes = convert_negatives(matrix)
    return passes - 1 if not contains_negative(matrix) else -1


def convert_negatives(matrix):
    next_queue = get_all_positive_positions(matrix)
    passes = 0

    while len(next_queue) > 0:
        current_queue = next_queue
        next_queue = []

        while len(current_queue) > 0:
            current_row, current_column = current_queue.pop(0)
            adjacent_positions = get_adjacent_positions(current_row, current_column, matrix)

            for position in adjacent_positions:
                row, column = position
                value = matrix[row][column]
                if value < 0:
                    matrix[row][column] *= -1
                    next_queue.append([row, column])
        passes += 1
    return passes


def get_all_positive_positions(matrix):
    positive_positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                positive_positions.append([row, col])
    return positive_positions


def get_adjacent_positions(row, col, matrix):
    adjacent_positions = []

    if row > 0:
        adjacent_positions.append([row - 1, col])

    if row < len(matrix) - 1:
        adjacent_positions.append([row + 1, col])

    if col > 0:
        adjacent_positions.append([row, col - 1])

    if col < len(matrix[0]) - 1:
        adjacent_positions.append([row, col + 1])

    return adjacent_positions


def contains_negative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


if __name__ == '__main__':
    matrix = [
        [0, -2, -1],
        [-5, 2, 0],
        [-6, -2, 0]
    ]
    result = minimum_passes_matrix(matrix)
    print(result)
