# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val)

        node = root
        while node:
            pre = node
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right

        if val < pre.val:
            pre.left = TreeNode(val)
        elif val > pre.val:
            pre.right = TreeNode(val)

        return root

"""
1. 根据二叉搜索树的性质遍历，即val<node.val访问node.left，val>node.val访问node.right;
2. 遍历至叶子节点，根据二叉搜索树性质进行插入节点，node.left/right = TreeNode(val).
"""
