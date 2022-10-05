"""双指针应用"""


# leetcode_27:
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.


def remove_element(nums, val):
    i_1 = 0
    i_2 = 0
    while i_1 < len(nums):
        if nums[i_1] != val:
            nums[i_2] = nums[i_1]
            i_2 += 1
        i_1 += 1
    return i_2


# leetcode_977:
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
# in non-decreasing order.


def sorted_squares(nums):
    n = len(nums)
    left, right, k = 0, n - 1, n - 1
    ans = [0] * n
    while left <= right:
        lm = nums[left] ** 2
        rm = nums[right] ** 2
        if lm >= rm:
            ans[k] = lm
            left += 1
        else:
            ans[k] = rm
            right -= 1
        k -= 1
    return ans
