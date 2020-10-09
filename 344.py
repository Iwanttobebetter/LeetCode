class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

"""
1. 左右两个指针分别指向字符串的最左端和最右端；
2. 左右指针位置的字符迭代互换至字符串中间，字符串反转完成。
"""