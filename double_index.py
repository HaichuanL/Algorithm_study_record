"""双指针应用"""


"""删除数组中指定值"""


def remove_element(nums, val):
    i_1 = 0
    i_2 = 0
    while i_1 < len(nums):
        if nums[i_1] != val:
            nums[i_2] = nums[i_1]
            i_2 += 1
        i_1 += 1
    return i_2


"""平方排序"""


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
