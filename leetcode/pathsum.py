# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.path_sum(root, targetSum, result)
        return result

    def path_sum(self, root, target_sum, result, path_list=[]):

        if not root:
            return

        if target_sum == root.val and not root.left and not root.right:
            result.append(path_list)
        else:
            self.path_sum(root.left, target_sum - root.val, result, path_list)
            self.path_sum(root.right, target_sum - root.val, result, path_list)

        path_list.pop()
