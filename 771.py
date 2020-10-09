class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not S or not J:
            return 0
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count

"""
1. 迭代字符串S，判断是否在J字符串集中；
2. 测试用例中貌似没有S或J空的情况，还是加上了判断。
"""
