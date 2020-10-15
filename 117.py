"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:

    def connect(self, root: 'Node') -> 'Node':

        current_node = root
        head = Node()
        next_node = head

        while current_node:
            if current_node.left:
                next_node.next = current_node.left
                next_node = current_node.left
            if current_node.right:
                next_node.next = current_node.right
                next_node = current_node.right

            current_node = current_node.next
            if not current_node:
                current_node = head.next
                head.next = None
                next_node = head

        return root


"""
填充每个节点的next指针指向其下一个右侧节点（如果没有右侧节点则为空）

1. 逐层遍历节点，同时使用next_node.next->对下层节点进行线性链接
2. 该层遍历结束，将head.next指向的下层最左头节点作为新的当前节点，重新开始遍历
3. 重复1、2步直到遍历结束，逐层的链接也完成
"""
