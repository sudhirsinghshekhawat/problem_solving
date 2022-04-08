# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        node = root
        while node:
            if val <= node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
            elif val >= node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
        return root
