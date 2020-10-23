# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node1, node2 = slow, slow.next
        slow.next = None
        while node2:
            tmp = node2.next
            node2.next = node1
            node1 = node2
            node2 = tmp

        node1, node2 = head, node1
        while node2 and node1:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True

"""
方法一：
1. 遍历至链表中点，将链表后半部分逆序，再与前半部分一一对比是否相同，问题解决。
"""