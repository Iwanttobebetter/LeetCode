
# 方法一：迭代重复字符串判断
class Solution:
    def commonChars(self, A: list[str]) -> list[str]:

        common_str = list(A[0])

        for s in A:
            s = list(s)
            for c in common_str[:]:
                if c not in s:
                    common_str.remove(c)
                    if not common_str:
                        return []
                else:
                    s.remove(c)
        return common_str

# 方法二：26位字符统计
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        common_str = [float('inf')] * 26

        for string in A:
            freq = [0] * 26
            for s in string:
                freq[ord(s) - ord('a')] += 1
            for i in range(26):
                common_str[i] = min(common_str[i], freq[i])

        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * common_str[i])

        return result


"""
统计多个字符串中的相同字符（重复相同的也重复统计，以最小的相同重复为准）

方法一：
1. 建立一个重复字符列表，初始化为第一个字符串；
2. 迭代每个字符串中对重复字符列表中每个可能重复的字符进行遍历；
3. 若该重复字符不在该字符串中出现，则从重复字符列表中删除该字符（删除至None直接返回空列表）；
4. 若该重复字符出现在该字符串中，则该字符串去除一个该重复字符（可能存在不同个该重复字符），继续遍历剩余可能重复字符。

方法二：
1. 建立一个26位的列表用来存储重复的小写字符每一个的数量；
2. 遍历每一个字符串，统计其各字符数；
3. 为了选择公共重复字符，与当前重复字符列表进行比较，更新每一个字符的数量；
4. 最后将统计好的，所有字符串公共重复的字符按其数量写入列表，即解决问题。
"""
