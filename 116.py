"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 方法一：
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        current_node = root
        head = Node()
        pre_node = head
        while current_node:
            if current_node.left:
                pre_node.next = current_node.left
                pre_node.next.next = current_node.right
                pre_node = current_node.right
            else:
                return root

            current_node = current_node.next
            if not current_node:
                current_node = head.next
                # head.next = None
                pre_node = head
        return root

# 方法二：
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        head = root
        while head.left:

            node = head
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            head = head.left
        return root


"""

方法一：
1. 由根节点开始逐层遍历节点，并将其下一层节点进行链接，由此迭代至下一层时可视作链表；
2. 由于是完美二叉树，因此对遍历到的每个节点均有node.left.next->node.right，节点间均有pre_node.right.next->node.left；
3. 迭代每个节点，其左孩子存在时，进行pre_node.next->node.left(.next)->node.right，若不存在则本层不存在，遍历结束，直接返回root；
4. 设置一个对于下一层的虚拟头节点head：①下层最左侧的节点也有了一个虚拟的pre_node，②在本层遍历结束后，下一层的开始节点即为head.next；
5. 通过判断node.left不存在（因为是完美二叉树，不存在时说明没有下一层，而本层已经通过上一层处理完成），因此可以退出循环，问题解决。

方法二：
1. 由根节点开始逐层遍历节点，并将其下一层节点进行链接，由此迭代至下一层时可视作链表；
2. 由于是完美二叉树，因此对遍历到的每个节点均有node.left.next->node.right，节点间均有pre_node.right.next->node.left；
3. 遍历本层链表时，每个节点的child节点间右->左可以通过node.next是否存在来进行node.right.next->node.next.left；
4. 本层遍历结束后，将head.left作为下一层的链表头节点继续进行遍历，即head=head.left，直到新head.left为None时则不存在下一层，问题解决。
"""