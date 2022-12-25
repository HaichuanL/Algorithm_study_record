"""leetcode_566: Reshape the Matrix
You are given an m x n matrix mat and two integers r and c representing the number of rows and
the number of columns of the wanted reshaped matrix.
If the reshape operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix."""
import numpy as np


def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        print('impossible reshape!!!')
        return mat
    whole_list = []
    mat_new = []
    first = 0
    for i in range(len(mat)):
        for j in mat[i]:
            whole_list.append(j)
    for i in range(c, len(whole_list) + 1, c):
        mat_new.append(whole_list[first: i])
        first = i
    return mat_new


if __name__ == '__main__':
    matrix = np.arange(1, 9).reshape(4, 2)
    print('original matrix:\n', matrix)
    new_matrix = matrix_reshape(matrix, 2, 4)
    print('new matrix:\n', new_matrix)
