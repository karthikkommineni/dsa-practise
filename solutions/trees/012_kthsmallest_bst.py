# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder traversal (sorted) → count nodes until kth
        self.counter = 0             # visited count
        self.res = None              # answer once found
        self.k = k                   # capture k for dfs
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None or self.res is not None:  # base + short-circuit if found
            return
        self.dfs(node.left)                       # left
        if self.res is not None:                  # re-check after left
            return
        self.counter += 1                         # visit current
        if self.counter == self.k:                # kth hit
            self.res = node.val
            return
        self.dfs(node.right)                      # right


"""
=========================
Quick Revision Notes
=========================

Trigger Thought:
👉 "BST inorder is sorted — count until k."

Logic Idea:
- Do inorder: left → root → right.
- Keep a counter of visited nodes.
- When counter == k → current node’s value is the answer.
- Short-circuit once found to avoid extra work.

Why it works:
- In BST, inorder traversal yields strictly increasing values.
- The kth visited node equals the kth smallest by definition.

Complexity:
- Time: O(h + k) average (O(n) worst if skewed).
- Space: O(h) recursion depth, h = tree height.

Pitfalls:
- Forgetting to stop after finding kth (adds unnecessary traversal).
- Storing result as 0 initially (0 can be valid) → use None until set.
- Losing access to k inside dfs if not captured (e.g., store as self.k or use closure).

---------------------------------
Java Reference (mental cross-check)
---------------------------------
class Solution {
    private int count = 0, ans = -1, K;

    public int kthSmallest(TreeNode root, int k) {
        this.K = k;
        dfs(root);
        return ans;
    }

    private void dfs(TreeNode n) {
        if (n == null || ans != -1) return;   // short-circuit once found
        dfs(n.left);
        if (ans != -1) return;
        if (++count == K) { ans = n.val; return; }
        dfs(n.right);
    }

    static class TreeNode {
        int val; TreeNode left, right;
        TreeNode(int v) { val = v; }
        TreeNode(int v, TreeNode l, TreeNode r) { val=v; left=l; right=r; }
    }
}
"""
