
# 方法一： 枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 方法二：查表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dic = {}
        for i, n in enumerate(nums):
            if target - n in nums_dic:
                return [nums_dic[target - n], i]
            nums_dic[nums[i]] = i
        return []


"""
方法二： 查表
1. 创建一个表用来存储迭代过的值与其索引；
2. 迭代过程中比较当前值是否存在已迭代过的值可以满足target求和要求。
"""
