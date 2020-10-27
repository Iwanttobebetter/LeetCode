# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []

        def pre_traversal(node):
            if not node:
                return
            node_list.append(node.val)
            pre_traversal(node.left)
            pre_traversal(node.right)

        pre_traversal(root)
        return node_list

# 方法二：迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return root

        value_list = []
        node_list = [root]
        while node_list:
            node = node_list.pop()
            value_list.append(node.val)
            if node.right:
                node_list.append(node.right)
            if node.left:
                node_list.append(node.left)
        return value_list

        # value_list = []
        # node_list = [root]
        # node = root
        # while node_list or node:
        #     while node:
        #         value_list.append(node.val)
        #         node_list.append(node)
        #         node = node.left
        #     node = node_list.pop()
        #     node = node.right
        # return value_list

"""
返回一个二叉树的前序遍历。

方法一：
1. 递归，存储每个遍历到的节点值，然后先进入left子节点，节点为空时返回，后进入right子节点，问题解决。

方法二：
1. 构建一个栈，迭代栈直至为空，迭代时弹出栈顶的节点存储其值，然后先将其右子节点入栈，再将其左子节点入栈，迭代结束，问题解决。
"""