# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一：
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        pre_list = set()
        while head is not None:
            if head in pre_list:
                return True
            pre_list.add(head)
            head = head.next

        return False


# 方法二：龟兔赛跑
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True

        # while fast is not None and fast.next is not None:
        #     if slow == fast:
        #         return True
        #     fast = fast.next.next
        #     slow = slow.next
        # return False


"""
方法一：
1. 通过哈希方式迭代存储遍历过的链表节点；
2. 查询当前节点是否已经遍历过来判断是否存在环。

方法二：
1. 通过slow、fast两个指针迭代链表；
2. fast指针比slow指针速度快，若存在环则存在fast==slow。
"""