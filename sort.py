"""Sort Algorithm"""


"""Bubble sort: 冒泡排序"""


#
def sorted_squares_bubble(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    for j in range(len(nums)-1, 0, -1):
        for i in range(j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums
