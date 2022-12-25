"""leetcode_378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix."""


def kth_smallest(matrix, k):
    n = len(matrix)
    left = 0
    right = n - 1
