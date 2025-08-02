"""
******** TIME & SPACE COMPLEXITY ********

Insert / Get / Remove:
- Average: O(log N) for balanced tree
- Worst:   O(N) if tree is skewed

Space:
- O(N) for storing all nodes

*****************************************
"""

# Binary Search Tree Node
class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

# Implementation for Binary Search Tree Map
class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root is None:
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val  # Update existing key
                return

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        current = self.root
        while current and current.right:
            current = current.right
        return current.val if current else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr is None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                # Swap with inorder successor (smallest in right subtree)
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> list[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: list[int]) -> None:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

"""
******************** LOGIC ********************

1. BST property: Left subtree < Root < Right subtree.
2. `insert`: Recursively walk and insert at correct location or update value.
3. `get`: Search for node by key.
4. `getMin` / `getMax`: Traverse left or rightmost paths.
5. `remove`: 
   - Case 1: No child → return None
   - Case 2: One child → return that child
   - Case 3: Two children → swap with inorder successor, then delete successor.
6. `getInorderKeys`: Get sorted order of all keys using in-order traversal.

***********************************************
"""
