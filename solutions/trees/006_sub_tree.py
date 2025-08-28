# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if not subRoot:
            return True
        if not root:
            return False

        # if current values match, check full tree equality here
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        # otherwise keep searching in left or right
        left_bool = self.isSubtree(root.left, subRoot)
        right_bool = self.isSubtree(root.right, subRoot)
        return left_bool or right_bool

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
