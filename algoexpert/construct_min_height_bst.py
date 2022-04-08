"""
construct a min height bst by given sorted array
"""


def min_height_bst_construction(array, start_idx, end_idx):
    if end_idx < start_idx:
        return None
    mid_idx = (start_idx + end_idx) // 2
    bst = BST(array[mid_idx])
    bst.left = min_height_bst_construction(array, start_idx, mid_idx - 1)
    bst.right = min_height_bst_construction(array, mid_idx + 1, end_idx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 22]
    bst = min_height_bst_construction(array, 0, len(array) - 1)
