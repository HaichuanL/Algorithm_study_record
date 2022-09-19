class Algo:
    '''Fibonacci'''
    def fibo(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.fibo(self, n=n - 1) + self.fibo(self, n=n - 2)

    def fibo_v2(self, first, second, n):
        if n == 0:
            return 0
        if n < 3:
            return 1
        elif n == 3:
            return first + second
        else:
            return self.fibo_v2(self, first=second, second=first+second, n=n-1)

    '''Binary search 二分查找(v1:左闭右闭，v2:左闭右开)
        tip1: 升序排列
        tip2: 无重复数据
        tip3: 时间复杂度为 O(logn)(计算最复杂的情况)'''
    def binary_search_v1(self, nums, target):
        """
            704: https://leetcode.cn/problems/binary-search/
            :type nums: List[int]
            :type target: int
            :rtype: int
            :vision: 1
        """
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


    def binary_search_v2(self, nums, target):
        """
            704: https://leetcode.cn/problems/binary-search/
            :type nums: List[int]
            :type target: int
            :rtype: int
            :vision: 2
        """
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

    '''双指针使用：删除数组中指定值
    tip1: 为什么要用覆盖'''
    def removeElement(self, nums, val):
        i_1 = 0
        i_2 = 0
        while i_1 < len(nums):
            if nums[i_1] != val:
                nums[i_2] = nums[i_1]
                i_2 += 1
            i_1 += 1
        return i_2


if __name__ == '__main__':
    algo = Algo
    '''Fibonacci'''
    # n = 40
    # fi = algo.fibo(algo, n=3)
    # print(fi)
    # fi_v2 = algo.fibo_v2(algo, first=1, second=1, n=3)
    # print(fi_v2)
    '''binary_search'''
    # nums = [4, 56, 78, 90, 299, 576, 2348, 7890]
    # target = 7890
    # bi_v1 = algo.binary_search_v1(algo, nums, target)
    # bi_v2 = algo.binary_search_v1(algo, nums, target)
    # print(bi_v1)
    # print(bi_v2)
    '''removeElement: 双指针'''
    nums = [4, 56, 78, 90, 299, 576, 2348, 7890]
    print('origin nums:', nums)
    val = 576
    rem = algo.removeElement(algo, nums, val)
    print('result:', nums)
    print(rem)
