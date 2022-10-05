"""recurrence: 递归"""


# Fibonacci using recurrence


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
        return self.fibo_v2(self, first=second, second=first + second, n=n - 1)
