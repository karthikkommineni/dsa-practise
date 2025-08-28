# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        # bfs - we use queue
        q = deque()
        q.append(root)
        res = []

        while len(q) > 0:
            lst = []
            for i in range(len(q)):
                curr = q.popleft()
                lst.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(lst)
        return res

