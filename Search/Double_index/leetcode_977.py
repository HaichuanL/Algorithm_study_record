"""leetcode_977:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
in non-decreasing order."""


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


if __name__ == '__main__':
    nums = [1, 5, 15, 33, 74, 95, 341]
    new_nums = sorted_squares(nums)
    print(new_nums)
