# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from ds_impl.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkHeightAndBalance(root)  != -1

    def checkHeightAndBalance(self,root):
        if not root:
            return 0
        left,right = self.checkHeightAndBalance(root.left), self.checkHeightAndBalance(root.right)
        if left == -1 or right == -1 or abs(left-right)>1:
            return -1
        return max(left,right)+1




class Solution2:
        def isBalanced(self, root: Optional[TreeNode]) -> bool:
            def dfs(root):
                if not root:
                    return [True, 0]

                left, right = dfs(root.left), dfs(root.right)
                balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
                return [balanced, 1 + max(left[1], right[1])]

            return dfs(root)[0]



    """
    abs(leftheight - rightHeight) > 1 -> return False

    challenge : pass through all nodes and find heights of subtrees for each node
    - if we compute heights separately for every node, that becomes O(n^2)

    solution : do one pass (bottom-up)
    - while computing height itself, also check if the subtree is balanced
    - if any subtree is unbalanced, return -1 and propagate upwards
    - else return height = 1 + max(leftHeight, rightHeight)

    so we determine imbalance from bottom while determining heights itself
    → final check: root != -1 means balanced
    """
