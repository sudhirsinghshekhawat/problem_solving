from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = None


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        tmp_arr = []
        result_arr = []
        queue = deque()
        queue.append(root)
        queue.append(None)

        while queue:
            tmp = queue.popleft()
            if tmp:
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                tmp_arr.append(tmp.val)
            else:
                if queue:
                    queue.append(None)
                result_arr.append(tmp_arr)
                tmp_arr = []
        return result_arr
