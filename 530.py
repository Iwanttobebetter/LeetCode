# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    pre_value = None
    min_value = float('inf')

    def getMinimumDifference(self, root: TreeNode) -> int:

        def pre_travel(node):
            if node is None:
                return

            pre_travel(node.left)
            if self.pre_value is None:
                self.pre_value = node.val
            else:
                self.min_value = min(node.val - self.pre_value, self.min_value)
                self.pre_value = node.val
            pre_travel(node.right)

        pre_travel(root)
        return self.min_value


"""
1. 二叉搜索树以中序遍历，节点值将以顺序增长的方式进行访问；
2. 由于升序排序后，任意两个值之差的最小绝对值一定是相邻两节点的差值；
3. 因此遍历过程中，以pre记录上一个访问节点，实时更新差的最小值即可实现。
"""