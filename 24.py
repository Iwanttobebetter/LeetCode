# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一：迭代判断
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        current = head
        while current and current.next:
            last = current.next
            if current is head:
                head = last
            else:
                pre.next = last

            current.next = last.next
            last.next = current
            pre = current
            current = current.next

        return head

# 方法二：首部添加一个虚拟节点
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        vir_head = ListNode(0)
        vir_head.next = head
        tmp = vir_head
        while tmp.next and tmp.next.next:
            node_1 = tmp.next
            node_2 = tmp.next.next

            tmp.next = node_2
            node_1.next = node_2.next
            node_2.next = node_1

            tmp = node_1

        return vir_head.next

# 方法三：递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        tail = head.next
        head.next = self.swapPairs(tail.next)
        tail.next = head

        return tail





"""
方法一：
1. 交换相邻两个节点，迭代判断当前节点与下一节点存在（包含了head与head.next为空的两种情况）；
2. 若当前交换节点为head节点，则需将head重新定位到两个节点中的last节点上，
3. 若交换节点不是head节点，则为链中两个节点进行交换，即pre->node_1->node_2交换node_1和2时，pre.next也需重新定位至node_2；
4. 完成迭代交换相邻节点与pre.next的更新，交换后的新链表完成。

方法二：
1. 设置一个虚拟节点在链表首部其next指向head节点；
2. 从head节点开始即为链中交换，即pre->node_1->node_2交换node_1和2时，pre.next重新定位至node_2;
3. 迭代直到没有成对的节点存在，链表交换完成，从vir_head.next处返回链表新的head节点。

方法三：
1. 递归整个链表直至没有成对的节点（没有节点或只有一个节点）；
2. 递归返回上一层，将上一层的head.next指向本层的节点对中的尾节点（即新的头节点），没有则指向None；
3. 将成对节点中的尾节点tail.next（即新的头节点）指向头节点，完成成对节点中的头尾互换；
4. 整个过程即是先成对地递归到链表的最尾部返回单个节点或None，然后上一层节点对中的head.next->尾部新链表的head节点，节点对的tail.next->head，最后tail作为尾部新链表的head节点返回。
"""