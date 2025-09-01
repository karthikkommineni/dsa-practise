# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional  # for hints only (keeps LeetCode-friendly)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        if not preorder or not inorder:              # base case: empty list => no node
            return None

        # logic/idea: root is first in preorder; split inorder around root into L-subtree and R-subtree
        root = TreeNode(preorder[0])                 # pick root from preorder[0]
        mid = inorder.index(root.val)                # find root position in inorder -> size of left subtree

        # slice arrays to pass each subtree's traversal pieces
        root.left  = self.buildTree(preorder[1:mid+1], inorder[:mid])        # left: next mid items in preorder, left half of inorder
        root.right = self.buildTree(preorder[mid+1:],  inorder[mid+1:])      # right: remaining preorder, right half of inorder
        return root


"""
Quick Revision Notes
--------------------
Trigger Thought:
- "Preorder picks root; inorder splits."

Logic Idea:
1) Root = preorder[0].
2) Find root index 'mid' in inorder.
3) Left subtree size = mid.
4) Recurse on:
   - Left: preorder[1 : mid+1], inorder[:mid]
   - Right: preorder[mid+1 : ], inorder[mid+1 : ]
5) Link and return.

Why it works:
- Preorder guarantees the first element is the current root.
- Inorder positions all left-subtree nodes before the root and right-subtree nodes after it.
- Splitting inorder by root uniquely partitions nodes; matching-sized slices from preorder align with those partitions.

Complexity:
- Time: O(n^2) in worst case (each recursion does an O(n) index() + slicing).  # acceptable for study; can optimize with a hashmap + indices.
- Space: O(n) recursion depth in skewed tree + O(n) for slices (implementation detail).

Pitfalls:
- Using `.index()` on inorder each time (O(n)) — fine here but slow for large inputs.
- Slicing creates copies; watch memory.
- Ensure base case when lists are empty.
- Works only if all node values are unique (required by classic problem).
"""

# ----------------------------
# Java Reference (just for mindset switch; not executed here)
# ----------------------------
# /*
# // Definition for a binary tree node.
# // public class TreeNode {
# //     int val;
# //     TreeNode left;
# //     TreeNode right;
# //     TreeNode() {}
# //     TreeNode(int val) { this.val = val; }
# //     TreeNode(int val, TreeNode left, TreeNode right) {
# //         this.val = val;
# //         this.left = left;
# //         this.right = right;
# //     }
# // }
#
# class Solution {
#     public TreeNode buildTree(int[] preorder, int[] inorder) {
#         // Wrapper to pass indices; mirrors Python logic conceptually
#         return helper(preorder, 0, preorder.length - 1,
#                       inorder,  0, inorder.length  - 1);
#     }
#
#     private TreeNode helper(int[] pre, int ps, int pe, int[] in, int is, int ie) {
#         if (ps > pe || is > ie) return null;                 // base case
#
#         TreeNode root = new TreeNode(pre[ps]);               // root from preorder start
#         int mid = is;
#         while (mid <= ie && in[mid] != root.val) mid++;      // find root in inorder (O(n))
#         int leftSize = mid - is;                              // size of left subtree
#
#         // Build left and right using index windows (no array copies)
#         root.left  = helper(pre, ps + 1, ps + leftSize, in, is, mid - 1);   // left slice
#         root.right = helper(pre, ps + leftSize + 1, pe,      in, mid + 1, ie); // right slice
#         return root;
#     }
# }
# */
