"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

# 方法一： 递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        value_list = []

        def post_traversal(node: TreeNode):
            if not node:
                return
            post_traversal(node.left)
            post_traversal(node.right)
            value_list.append(node.val)

        post_traversal(root)

        return value_list

# 方法二： 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        value_list = []
        node_list = [root]
        travered_list = []

        while node_list:
            node = node_list[-1]
            if node.left and (node.left not in travered_list):
                node_list.append(node.left)
                continue
            if node.right and (node.right not in travered_list):
                node_list.append(node.right)
                continue
            value_list.append(node.val)
            travered_list.append(node_list.pop())

        return value_list



"""
方法二：
1. 以后序遍历的方式迭代遍历整个树的节点，即以“左右中”顺序访问节点；
2. 由根部遍历至最左端“未访问”过的路径，并存储该条路径；
3. 将“最左未访问路径”底部的节点值进行存储，并标记该节点为“已访问”；
4. 将已访问的节点弹出“最左未访问路径栈”，回到上一层未访问的节点，并继续遍历其余“未访问”的分支；
5. 重复34步，直到“路径栈”为空，即迭代到所有节点均以“左右中”的方式进行访问过。
"""
