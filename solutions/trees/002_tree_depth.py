from typing import Optional

from ds_impl.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left, right = 0, 0

        if not root:
            return 0                                # base: empty tree = depth 0

        if root.left:
            left = self.maxDepth(root.left)         # recurse left subtree

        if root.right:
            right = self.maxDepth(root.right)       # recurse right subtree

        return max(left, right) + 1                 # node depth = 1 + deeper side


"""
Logic / Main Idea:
- Depth at a node = 1 + max(depth of left, depth of right)
- Base case: null node has depth 0
- Final answer = depth of root (max depth of whole tree)
"""