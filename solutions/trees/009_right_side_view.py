# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])

        while len(q) > 0:  # there are ele in queue
            res.append(q[-1].val)
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

        return res


"""
- 1
-2, 3



"""




