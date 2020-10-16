
# 方法一：双指针
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        n = len(A)
        start, end, i = 0, n - 1, n - 1
        result = [0] * n
        while start <= end:
            if -A[start] > A[end]:
                result[i] = A[start] ** 2
                start += 1
            else:
                result[i] = A[end] ** 2
                end -= 1
            i -= 1
        return result

# 方法二：python排序
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([a**2 for a in A])

"""
给定一个非递减顺序排序的整数数组，返回每个数字的平方组成的新数组（按非递减顺序）。 

方法一：
1. 由于是非递减顺序的数列，设置两个指针分别从右两端开始向内移动，即两个指针分别代表负数和正数数列平方和的从小到大；
2. 不断迭代比较两个指针处数值平方后的大小，大的则按序列顺序从后向前存储，即问题解决。

方法二：
1. 迭代求出数列每个数的平方和，然后使用python内置排序函数，问题解决。
"""