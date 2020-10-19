
# 方法一：入栈出栈
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def handle_str(string: str):
            new_str = ''
            for ch in string:
                if ch != '#':
                    new_str += ch
                else:
                    new_str = new_str[:-1]
            return new_str

        return handle_str(S) == handle_str(T)



"""
给定两个含退格符（退格符#可以删去前一个字符）的字符串，判断两个字符串是否相同。

方法一：
1. 分别遍历两个字符串，逐个字符判断，字符则推入栈中，退格符#则从栈中弹出栈顶字符；
2. 遍历完成则退格符及应被删除的字符去除，比较还原后的字符串是否相同，问题解决。
"""