"""leetcode_485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array."""
import numpy as np


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


if __name__ == '__main__':
    nums = np.zeros((4, 8))
    nums[1: -1, 1: -1] = 1
    nums = nums.ravel()
    print(nums)
    max_len = find_max_consecutive_ones(nums)
    print(max_len)
