
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一：遍历存储（栈，数组）
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_dic = {}
        node, index = head, 0
        while node:
            node_dic[index] = node
            node = node.next
            index += 1
        if index-n-1 < 0:
            head = head.next
        else:
            node_dic[index-n-1].next = node_dic[index-n].next
        return head


# 方法二：快慢指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dumm_node = ListNode(0, head)
        fast, slow = head, dumm_node

        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dumm_node.next

"""
删除链表倒数第n个节点

方法一：
1. 遍历一遍链表，存储链表长度，并根据索引index-n-1找到倒数第n个节点的前驱节点进行删除，问题解决。

方法二：
1. 设置一个哑节点在head前，由此head节点也可当作链表中普通节点进行相同操作；
2. 设置快慢两个指针指向head，首先使fast先遍历n个节点，即此时fast与slow之间存在n-1个节点；
3. 由此当fast遍历到链表末端.next的None节点退出遍历时，slow恰好时链表倒数第n个节点（slow后有n-1个节点）；
4. 因此使slow初始指向head的虚拟前驱节点dumm_node，则遍历结束时slow指向倒数第n个节点的前驱节点，修改指向进行删除，问题解决。
"""
