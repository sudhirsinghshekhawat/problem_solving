def find_max_path_sum(tree):
    if tree is None:
        return (0, float("-inf"))
    left_max_branch, left_max_path = find_max_path_sum(tree.left)
    right_max_branch, right_max_path = find_max_path_sum(tree.right)
    max_child_branch = max(left_max_branch, right_max_branch)

    value = tree.value
    max_sum_branch = max(value, max_child_branch + value)
    max_sum_branch_as_root = max(left_max_branch + value + right_max_branch, max_sum_branch)
    max_path_sum = max(left_max_path, right_max_path, max_sum_branch_as_root)
    return max_sum_branch, max_path_sum


def maxPathSum(tree):
    _, max_path_sum = find_max_path_sum(tree)
    return max_path_sum
