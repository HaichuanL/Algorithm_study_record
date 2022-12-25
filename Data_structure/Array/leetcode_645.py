"""leetcode_645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array."""


def find_error_nums(nums):
    # 排序后
    # 重复的数字只需要循环就可以发现
    # 丢失的数字则需要分成三种情况，一种是丢失数字位于头，第二种丢失数字位于尾，第三种丢失数字是处于两差为2的相邻数字之间的数字
    nums.sort()
    ln = len(nums)
    repeat = -1
    lose = -1
    if nums[0] != 1:
        lose = 1
    elif nums[-1] != ln:
        lose = ln
    for i in range(ln):
        if nums[i] == nums[i - 1]:
            repeat = nums[i]
        if nums[i] - nums[i - 1] == 2:  # 丢失的数字是当相邻两数相差2时，得以发现
            lose = nums[i] - 1
    return [repeat, lose]


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 5, 7]
    result = find_error_nums(nums)
    print(result)
