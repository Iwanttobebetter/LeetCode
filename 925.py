
# 方法一：双指针
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i, j, n_nums, t_nums = 0, 0, len(name), len(typed)

        while j < t_nums:
            if i < n_nums and typed[j] == name[i]:
               i += 1
               j += 1
            elif i > 0 and typed[j] == name[i-1]:
                j += 1
            else:
                return False
        return i == n_nums


"""
检测可能存在长按键入的tpyed是否为正确的name键入，如 name = "alex", typed = "aaleex" -> True。

方法一：
1. 设置两个指针t、n记录tpyed与name的索引，以typed的字符数为退出循环判断，若tpyed[t]==name[n]且n<len(name),则索引同时后移一位；
2. 若tpyed[t]！=name[n]则判断typed[t]与name[n-1]，相同则t后移一位继续循环，不同说明并非长按导致的字符不同，返回False，问题解决；
3. 完成循环则typed全部迭代，若i为name的字符长度则说明全部匹配返回True，不同说明tpyed长度小于name，显然不匹配返回False，问题解决。
"""