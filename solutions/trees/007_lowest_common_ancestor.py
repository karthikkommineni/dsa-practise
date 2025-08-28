# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base case - both numbers found
        # logic build ancestral array, find difference

        if not root:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root
"""
- In a BST:
  * if root < p and root < q -> LCA in right subtree
  * if root > p and root > q -> LCA in left subtree
  * else (split or equality) -> current root is LCA




"""