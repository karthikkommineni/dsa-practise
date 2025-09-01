# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ds_impl.binary_tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.check_good_node(root, -float('inf'))
        return self.count

    def check_good_node(self, node: TreeNode, max_ele: int):
        if not node:
            return
        new_max_ele = max_ele
        if node.val >= max_ele:
            new_max_ele = node.val
            self.count += 1
        if node.left:
            self.check_good_node(node.left, new_max_ele)
        if node.right:
            self.check_good_node(node.right, new_max_ele)

"""
-key is figuring out the helper method that will traverse the tree



"""