"""array: 数组(以list的形式存在)"""


# leetcode_283:
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
def move_zero(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums


# leetcode_209: Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of
# a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
def min_subarray_len(target, nums):
    i_1 = 0
    i_2 = 0
    len_list = []
    while i_1 < len(nums):
        print(nums[i_2: i_1 + 1])
        if sum(nums[i_2: i_1 + 1]) >= target:
            len_list.append(i_1 + 1 - i_2)
        if sum(nums[i_2: i_1 + 1]) > target:
            i_1 = i_2 + 1
            i_2 += 1
        i_1 += 1
    if len(len_list) == 0:
        return 0
    else:
        return min(len_list)


# leetcode_566: Reshape the Matrix
# You are given an m x n matrix mat and two integers r and c representing the number of rows and
# the number of columns of the wanted reshaped matrix.
# If the reshape operation with given parameters is possible and legal,
# output the new reshaped matrix; Otherwise, output the original matrix.
def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    whole_list = []
    mat_new = []
    first = 0
    for i in range(len(mat)):
        for j in mat[i]:
            whole_list.append(j)
    for i in range(c, len(whole_list) + 1, c):
        print(first)
        mat_new.append(whole_list[first: i])
        first = i
    return mat_new


# leetcode: 485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
def find_max_consecutive_ones(nums):
    i_1 = 0
    i_2 = 0
    max_len = 0  # 让目前最大的长度与当前1的长度对比，省去全部存列表再比较
    while i_1 < len(nums):
        if nums[i_2] == 1 and nums[i_1] == 1:
            max_len = max(max_len, i_1 + 1 - i_2)  # i_1与i_2之间的长度需要i_1+1减去i_2
        elif nums[i_1] == 0:
            i_2 = i_1 + 1
        i_1 += 1
    return max_len


# leetcode_240. Search a 2D Matrix II
# Write an efficient algorithm that searches for a value target in an m x n integer matrix.
# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    row = 0  # 取最小的一行
    col = n - 1  # 取该行最大的值与target比较，比target大就在本行找，比target小就去下一行
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


# leetcode_378. Kth Smallest Element in a Sorted Matrix
# Given an n x n matrix where each of the rows and columns is sorted in ascending order,
# return the kth smallest element in the matrix.
def kth_smallest(matrix, k):
    n = len(matrix)
    left = 0
    right = n - 1


# leetcode_645. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
def find_error_nums(nums):
    # 排序后
    # 重复的数字只需要循环就可以发现
    # 丢失的数字则需要分成三种情况，一种是丢失数字位于头，第二种丢失数字位于尾，第三种丢失数字是处于两差为2的相邻数字之间的数字
    nums.sort()
    ln = len(nums)
    repeat = -1
    lose = -1
    if nums[0] != 1:
        lose = 1
    elif nums[-1] != ln:
        lose = ln
    for i in range(ln):
        if nums[i] == nums[i - 1]:
            repeat = nums[i]
        if nums[i] - nums[i - 1] == 2:  # 丢失的数字是当相邻两数相差2时，得以发现
            lose = nums[i] - 1
    return [repeat, lose]


# leetcode_287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
def find_duplicate(nums):
    ln = len(nums)
    nums.sort()
    duplicate = 0
    for i in range(ln):
        if nums[i] == nums[i - 1]:
            duplicate = nums[i]
    return duplicate


# 


if __name__ == '__main__':
    '''move_zero'''
    # nums = [1, 0, 9, 0, 8]
    # print(move_zero(nums))
    '''min_subarray_len'''
    # nums = [1, 2, 3, 4, 5]
    # print(min_subarray_len(11, nums))
    '''matrix_reshape'''
    # mat = [[1, 2, 3, 4], [3, 4, 7, 8]]
    # r = 4
    # c = 2
    # print(matrix_reshape(mat, r, c))
    '''find_max_consecutive_ones'''
    # nums = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
    # print(find_max_consecutive_ones(nums))
    '''search_matrix'''
    # matrix = [[1, 2, 3], [4, 5, 6]]
    # print(search_matrix(matrix, 4))
    '''find_error_nums'''
    # nums = [4, 2, 1, 3, 2]
    # print(find_error_nums(nums))
    '''find_duplicate'''
    # nums = [2, 3, 4, 2, 1]
    # print(find_duplicate(nums))
