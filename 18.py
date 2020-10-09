class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        four_list = []
        length = len(nums)
        if not nums or length < 4:
            return four_list

        nums.sort()
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 1] + nums[length - 2] + nums[length - 3] < target:
                continue

            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 1] + nums[length - 2] < target:
                    continue

                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        four_list.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        right == 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return four_list

"""
1. 为了避免遍历出的四元组重复，首先将nums进行排序；
2. 三层遍历，当满足total == target时，将该顺序的四元组存储下来；
3. 进行优化，由于nums进行了排序：
    Ⅰ. 当最小的连续四项和大于target时，即剩余所有可能均>target，可退出遍历；
    Ⅱ. 当前值与三项最大数求和小于target时，即剩余所有可能均<target，可跳过当前循环；
    Ⅲ. 第二层循环同理。
"""
