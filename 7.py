

# 方法一：
class Solution:
    def reverse(self, x: int) -> int:

        res = str(abs(x))[::-1]
        res = int(res) if x > 0 else -int(res)
        if -(1<<31) < res < (1<<31)-1:
            return res
        return 0

# 方法二：
class Solution:
    def reverse(self, x: int) -> int:

        y, res = abs(x), 0
        max_num = (1<<31)-1 if x > 0 else (1<<31)
        while y != 0:
            res = res*10 + y%10
            if res > max_num:
                return 0
            y //= 10
        return res if x > 0 else -res

"""
给定一个32位有符号整数，对整数进行反转（反转后整数溢出则返回0）。

方法一：
1. 将x的绝对值转为字符串进行反转，然后添加正负号；
2. 判断反转后的数字范围是否溢出32位有符号整型，溢出返回0.

方法二：
1. 对整数x取绝对值后，从后到前进行逐个数字的弹出，然后推入反转数字res中，即实现正整数的反转；
2. 具体过程：取y为x绝对值->y%10（即弹出最后一位数字）->res*10+弹出数字（即推入到res中）->y//10（即去除最后一位数字）；
4. 迭代过程中，不断迭代直到y为0，x的绝对值反转完成，同时对res进行判断是否小于1<<31-1或1<<31（取决于x正数或负数），若小于则溢出范围，直接返回0；
5. 迭代完成后，对x进行判断，返回正res或-res，问题解决。
"""




