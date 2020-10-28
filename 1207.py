

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        num_count = {}
        for n in arr:
            if n not in num_count.keys():
                num_count[n] = 0
            else:
                num_count[n] += 1
        return len(num_count.values()) == len(set(num_count.values()))


"""
给定一个整数数组，统计每个数出现的次数，若次数均不同则true，反之为false。

1. 用一个hash表统计每个数出现的次数，比较该hash表的元素长度与转为集合类型后的元素长度是否一致，问题解决。
"""