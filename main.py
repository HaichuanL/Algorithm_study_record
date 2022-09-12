class Algo:
    # Fibonacci
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

    # Binary search 二分查找
    def binary_search(self):
        """
            704: https://leetcode.cn/problems/binary-search/
            :type nums: List[int]
            :type target: int
            :rtype: int
        """
        print('')


if __name__ == '__main__':
    algo = Algo
    # Fibonacci
    n = 40
    fi = algo.fibo(algo, n=3)
    print(fi)
    fi_v2 = algo.fibo_v2(algo, first=1, second=1, n=3)
    print(fi_v2)
