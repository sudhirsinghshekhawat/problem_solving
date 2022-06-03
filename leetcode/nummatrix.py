from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.data = [[0 for _ in range(cols + 1)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                self.data[row][col + 1] = self.data[row][col] + matrix[row][col]

    def sum_region(self, row1, col1, row2, col2):
        result = 0
        for row in range(row1, row2 + 1):
            result += (self.data[row][col2 + 1]) - self.data[row][col1]
        return result
