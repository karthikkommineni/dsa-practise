# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start recursion with full valid range (-∞, +∞)
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, left, right):
        if node is None:
            return True
        if not left < node.val < right:   # Node must strictly lie within (left, right)
            return False
        left_node_bool = self.helper(node.left, left, node.val)       # Left subtree must be within (left, node.val)
        right_node_bool = self.helper(node.right, node.val, right)   # Right subtree must be within (node.val, right)
        return left_node_bool and right_node_bool


"""
=========================
Quick Revision Notes
=========================

Trigger Thought:
👉 "Each node must fit inside a valid range — update that range as we go down."
" every node based on left or right subtree - val should be < or > parent node

Logic Idea:
- For BST: left < node < right.
- Pass down updated bounds (min, max).
- Left child → high = parent value.
- Right child → low = parent value.

Why it works:
- Checks all nodes against ancestor constraints, not just parent.
- Prevents hidden violations deep in subtrees.

Complexity:
- Time: O(n) → visit each node once.
- Space: O(h) → recursion depth.

Pitfalls:
- Use STRICT < , duplicates are invalid.
- Don’t just compare with parent → must carry full bounds.
"""
