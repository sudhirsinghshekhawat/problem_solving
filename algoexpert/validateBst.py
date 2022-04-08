class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validate_bst_helper(tree, float("-inf"), float("inf"))


def validate_bst_helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False

    return validate_bst_helper(tree.left, min_value, tree.value) and validate_bst_helper(tree.right, tree.value,
                                                                                         max_value)
