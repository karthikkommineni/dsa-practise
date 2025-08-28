from collections import deque
from typing import Optional

from ds_impl.binary_tree import TreeNode


class Solution:
    def invertTree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    class Solution:
        def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return None
            q = deque([root])

            while q:
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            return root

