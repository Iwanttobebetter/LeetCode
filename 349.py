
# 方法一：
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([i for i in nums1 if i in nums2]))

# 方法二：排序+双指针
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        nums = []
        i, j = 0, 0
        len_n1, len_n2 = len(nums1), len(nums2)
        while i < len_n1 and j < len_n2:
            n1, n2 = nums1[i], nums2[j]
            if n1 < n2:
                i += 1
            elif n1 > n2:
                j += 1
            else:
                if not nums or n1 != nums[-1]:
                    nums.append(n1)
                i += 1
                j += 1
        return nums

"""
计算两个数组的交集。

方法一：
1. 迭代num1中的元素若存在num2中则加入列表，列表转集合去重，最后转为列表返回，问题解决。

方法二：
1. 两个数组进行排序，然后设置两个指针从头开始遍历比较，较小的则后移，相同则判断是否添加入nums中（nums中是否已存在）并同时后移，迭代至任一数组遍历结束，问题解决。
"""