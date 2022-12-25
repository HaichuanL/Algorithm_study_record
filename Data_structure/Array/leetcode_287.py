"""leetcode_287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space."""
import numpy as np


def find_duplicate(nums):
    ln = len(nums)
    nums.sort()
    duplicate = 0
    for i in range(ln):
        if nums[i] == nums[i - 1]:
            duplicate = nums[i]
    return duplicate


if __name__ == '__main__':
    nums = np.arange(1, 11)
    nums = np.append(nums, 4)
    print(nums)
    duplicate = find_duplicate(nums)
    print(duplicate)
