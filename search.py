"""Search Algorithm"""

"""Binary search 二分查找(v1:左闭右闭，v2:左闭右开)
    tip1: 升序排列
    tip2: 无重复数据
    tip3: 时间复杂度为 O(logn)(计算最复杂的情况)"""


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


# binary_search leetcode_35
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
