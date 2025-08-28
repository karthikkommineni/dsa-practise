from typing import Optional

from ds_impl.binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        def dfs(curr):
            if not curr:
                return 0                         # base: height of empty tree = 0

            left = dfs(curr.left) if curr.left else 0   # height of left subtree
            right = dfs(curr.right) if curr.right else 0 # height of right subtree

            self.max_dia = max(self.max_dia, left + right)  # update diameter

            return max(left, right) + 1           # height of current node

        dfs(root)
        return self.max_dia



    """
     calculate diameter at each node = max(left)+max(right) 
     - calcutae result = max diameter -> so max(dia) at each node
     
     
     logic:
     - Diameter at each node = left height + right height
- Update global max with this diameter
- Height of node = 1 + max(left, right)
- Final answer = maximum diameter found


    """