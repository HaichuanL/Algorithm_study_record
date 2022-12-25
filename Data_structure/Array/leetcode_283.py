"""leetcode_283:
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements."""


def move_zero(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums


if __name__ == '__main__':
    nums = [0, 0, 1, 3, 4, 5]
    new_nums = move_zero(nums)
    print(new_nums)
