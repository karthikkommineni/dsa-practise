from ds_impl.binary_tree import TreeNode

class BST:
    # --- Search ---
    @staticmethod
    def search(root: TreeNode, target: int) -> bool:
        if not root:
            return False
        if target > root.val:
            return BST.search(root.right, target)   # recurse right
        elif target < root.val:
            return BST.search(root.left, target)    # recurse left
        else:
            return True                             # found

    # --- Insert ---
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)  # go right
        else:
            root.left = self.insertIntoBST(root.left, val)    # go left
        return root

    # --- Min Value Node ---
    @staticmethod
    def min_value_node(node: TreeNode) -> TreeNode:
        """Return left-most (smallest) node in subtree."""
        while node.left:
            node = node.left
        return node

    # --- Remove ---
    @staticmethod
    def remove(root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if val < root.val:
            root.left = BST.remove(root.left, val)
        elif val > root.val:
            root.right = BST.remove(root.right, val)
        else:
            # Node found
            if not root.left:
                return root.right    # replace with right
            elif not root.right:
                return root.left     # replace with left
            else:
                succ = BST.min_value_node(root.right)   # inorder successor
                root.val = succ.val                     # copy successor
                root.right = BST.remove(root.right, succ.val)  # delete successor
        return root
