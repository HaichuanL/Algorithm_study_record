"""leetcode_27:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place."""


def remove_element(nums, val):
    i_1 = 0
    i_2 = 0
    new_nums = nums.copy()
    while i_1 < len(new_nums):
        if new_nums[i_1] != val:
            new_nums[i_2] = new_nums[i_1]
            i_2 += 1
        i_1 += 1
    new_nums = new_nums[:i_2]
    return new_nums


if __name__ == '__main__':
    nums = [2, 3, 5, 1, 2, 5]
    val = 5
    new_nums = remove_element(nums, val)
    print(new_nums)
    # print(nums)
