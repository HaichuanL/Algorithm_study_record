"""leetcode_209: Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of
a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead."""


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


if __name__ == '__main__':
    nums = [2, 5, 3, 5, 7, 8, 2]
    length = min_subarray_len(21, nums)
    print(length)
