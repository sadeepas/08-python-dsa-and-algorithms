"""
Binary Search Tree (BST) Implementation with In-Order Traversal
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, val: int):
        self.root = self._insert_node(self.root, val)

    def _insert_node(self, node: Optional[TreeNode], val: int) -> TreeNode:
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_node(node.left, val)
        elif val > node.val:
            node.right = self._insert_node(node.right, val)
        return node

    def inorder(self) -> List[int]:
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)
        traverse(self.root)
        return result

if __name__ == "__main__":
    bst = BinarySearchTree()
    for item in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(item)
    print("In-order sorted traversal of BST:", bst.inorder())
