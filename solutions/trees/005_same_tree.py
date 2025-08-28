# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from ds_impl.binary_tree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # every node == counterpart, left,right,val same -true

        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q: 
            return False

        left_bool =   self.isSameTree(p.left,q.left)
        right_bool =  self.isSameTree(p.right,q.right)
        if p.val == q.val and left_bool and right_bool:
            return True
        else:
            return False










