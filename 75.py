
# 方法一： 两次遍历，一次存储
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pre0, pre1 = 0, 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[pre1], nums[i] = nums[i], nums[pre1]
                pre1 += 1
            elif nums[i] == 0:
                nums[pre0], nums[i] = nums[i], nums[pre0]
                if pre0 < pre1:
                    nums[pre1], nums[i] = nums[i], nums[pre1]
                pre0 += 1
                pre1 += 1

# 方法二： 0、1指针一次遍历，交换存储
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                if nums[i] != 1:
                    continue
            i += 1

# 方法三： 前、后指针一次遍历，交换存储
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                if nums[i] != 1:
                    continue
            i += 1
"""
方法一：
1. 第一次遍历存储各值（0、1、2）数量；
2. 第二次遍历根据各值数量，按顺序重新给存储赋值。

方法二：
1. 两个指针标记交换至0和1的两个位置；
2. 由于0在1前，num[i]为0时判断pre0<pre1（存在1已排好序，需pre0<->num[i]后，将pre0处的1交换回pre1位置，即num[i]<->pre1），
    由于插入一个0在0序列后与1序列前，因此无论是否pre0<pre1，均需0、1指针自增1；
3. 0与1在列表内交换排序好之后，2也自动排序结束。

方法三：
1. 两个指针标记插入left和right的两个位置，num[i]为0则交换至left，为2则交换至right；
2. 交换2后由于right处值未知，nums[i]不为1时，则不改变遍历指针i的位置重新进行交换操作；
3. 当所有0排序至最left，所有2排序至最right，则1也自动排序至其两者中间。
"""
