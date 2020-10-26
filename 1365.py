


# 方法一：暴力迭代
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums_size = len(nums)
        nums_list = [0]*nums_size
        for i in range(nums_size):
            for j in range(nums_size):
                if nums[j] < nums[i]:
                    nums_list[i] += 1
        return nums_list

# 方法二：计数排序
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums_list = []
        nums_count = [0]*101
        for n in nums:
            nums_count[n] += 1
        for i in range(1,101):
            nums_count[i] += nums_count[i-1]
        for n in nums:
            nums_list.append(nums_count[n-1] if n!=0 else 0)
        return nums_list

"""
给定数组nums，对于其中每个元素，统计数组中比其小的所有数字的数目。

方法一:
1. 双层迭代，判断每个元素比其小的数字个数并存储，返回结果问题解决。

方法二：
2. 计数排序，对每种可能结果进行计数，然后采用前缀和进行存储，则比其小的数字数目为其索引的前一个元素（比0小的为0），问题解决。
"""