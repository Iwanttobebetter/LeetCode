# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一：线性表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        node_list = [head]
        while node_list[-1].next:
            node_list.append(node_list[-1].next)

        start, end = 0, len(node_list) - 1
        while start + 1 < end:
            node_list[start].next = node_list[end]
            node_list[end].next = node_list[start + 1]
            start += 1
            end -= 1
        node_list[end].next = None


# 方法二：链表中点+链表逆序+链表合并
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        end, mid = head, head

        while end and end.next:
            end = end.next.next
            mid = mid.next

        node1, node2 = mid, mid.next
        mid.next = None
        while node2:
            tmp = node2
            node2 = tmp.next
            tmp.next = node1
            node1 = tmp

        node1, node2 = head, node1
        while node1 and node1.next != node2:
            next_node1 = node1.next
            next_node2 = node2.next
            node1.next = node2
            node2.next = next_node1
            node1 = next_node1
            node2 = next_node2

"""
给定一个单链表L：L0→L1→…→Ln-1→Ln，将其重新排列后变为：L0→Ln→L1→Ln-1→L2→Ln-2→…

方法一：
1. 用列表存储链表节点，设置首尾两个索引迭代向链表中间遍历节点，并修改其next指向，问题解决。

方法二：
1. 首先使用快慢指针遍历找到链表中点，并分成两个链表；
2. 将后半部分链表进行逆序反转；
3. 迭代遍历两个链表中的元素，依次合并节点，问题解决。
"""





