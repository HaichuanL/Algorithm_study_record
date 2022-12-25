"""leetcode_240. Search a 2D Matrix II
Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom."""
import numpy as np


def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    row = 0  # 取最小的一行
    col = n - 1  # 取该行最大的值与target比较，比target大就在本行找，比target小就去下一行
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


if __name__ == '__main__':
    matrix = np.arange(1, 10).reshape(3, 3)
    print(matrix)
    index = search_matrix(matrix, 7)
    print(index)
