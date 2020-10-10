# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        pre_list = set()
        while head is not None:
            if head in pre_list:
                return head
            pre_list.add(head)
            head = head.next

        return None

"""
方法一：
1. 通过哈希方式迭代存储遍历过的链表节点；
2. 若当前节点已经遍历过，则存在环,且当前节点为入环第一个节点。
"""