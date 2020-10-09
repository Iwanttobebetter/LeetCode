"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:

        path_list = []
        sum_list = []

        def pre_travel(node: TreeNode, total: int):
            if not node:
                return

            path_list.append(node.val)
            total -= node.val
            if not node.left and not node.right and total == 0:
                sum_list.append(path_list[:])

            pre_travel(node.left, total)
            pre_travel(node.right, total)

            path_list.pop()

        pre_travel(root, total)
        return sum_list

"""
1. 采用递归进行前序遍历，并存储当前遍历的路径，每访问一个节点进行求和（与目标数相减）；
2. 当达到叶子节点，同时节点总和为目标数（目标数减至0），该路径存储为目标路径；
3. 从遍历队列中弹出访问完的节点，继续遍历下一个分支的路径并进行判断；
4. 直到所有根到叶子节点的路径遍历结束，输出符合的路径列表。
"""
