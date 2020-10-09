# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        flag = 0
        head_node = None
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + flag
            if total > 9:
                total = total % 10
                flag = 1
            else:
                flag = 0
            if not head_node:
                head_node = ListNode(total)
                new_node = head_node
            else:
                new_node.next = ListNode(total)
                new_node = new_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if flag == 1:
            new_node.next = ListNode(1)

        return head_node

"""
1. 迭代遍历两个链表，逐位求和；
2. 由于两个链表不一定同长度，为短链表不足位置补0进行迭代求和运算。
3. flag为进位标志，最后遍历结束若还有进位则补一个ListNode。
"""
