"""Search Algorithm"""

"""Binary search 二分查找(v1:左闭右闭，v2:左闭右开)
    tip1: 升序排列
    tip2: 无重复数据
    tip3: 时间复杂度为 O(logn)(计算最复杂的情况)"""


# leetcode_704:
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1
def binary_search_v1(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_v2(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    return -1


# leetcode_35:
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, /n
# return the index where it would be if it were inserted in order.
def search_insert(nums, target):
    l = 0
    r = len(nums) - 1
    if target in nums:
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
    else:
        if target > nums[r]:
            return len(nums)
        elif target < nums[l]:
            return 0
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
