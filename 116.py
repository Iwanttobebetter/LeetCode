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

# 方法三：递归
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs_travel(curr_node, next_node):
            if curr_node is None:
                return

            curr_node.next = next_node
            dfs_travel(curr_node.left, curr_node.right)
            dfs_travel(curr_node.right, None if curr_node.next == None else curr_node.next.left)

        dfs_travel(root, None)
        return root

"""
填充完美二叉树每个节点的next指针指向其下一个右侧节点（如果没有右侧节点则为空）

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

方法三：
1. 深度优先搜索递归，由于是完美二叉树，node.left若存在则一定有node.left.next->node.right；
2. 首先递归至树的最左端，进行左孩子的递归至叶子然后进行右孩子的判断，同时对每个经过的节点都使其与右侧节点进行链接（右侧没有则指向None）；
3. curr_node.left递归一定存在右侧的curr_node.right进行链接；
4. curr_node.right递归，由于是逐层链接递归至下方，因此递归的上一层若curr_node右侧节点存在，则已被curr_node.next所指向，若不存在则指向None；
5. 使curr_node.right右孩子与curr_node.next.left（右侧节点的左孩子）或None（curr_node.next不存在，curr_node.right为该层最后一个）相链接；
6. 深度优先搜索递归先左后右逐层向上，直至所有节点的右侧被指向，问题解决。
"""