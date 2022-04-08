from trees.BinaryTree import BinaryTreeNode, TreeTraversal


def create_bst() -> BinaryTreeNode:
    root = BinaryTreeNode(7)
    root.left = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(5)
    root.right = BinaryTreeNode(9)
    root.right.left = BinaryTreeNode(8)
    root.right.right = BinaryTreeNode(11)
    return root


def find_in_bst(root: BinaryTreeNode, val: int) -> bool:
    if root is None:
        return False
    if root.data == val:
        return True
    if root.data > val:
        return find_in_bst(root.left, val)
    else:
        return find_in_bst(root.right, val)


def find_min_in_bst(root: BinaryTreeNode) -> bool:
    if root is None:
        return 0
    if root.left is None:
        return root.data
    return find_min_in_bst(root.left)


def find_max_in_bst(root: BinaryTreeNode) -> bool:
    if root is None:
        return 0
    if root.right is None:
        return root.data
    return find_max_in_bst(root.right)


def insert_into_bst(root: BinaryTreeNode, data: int):
    node = BinaryTreeNode(data)
    if root is None:
        root = node
    else:
        if data > root.data:
            root.right = insert_into_bst(root.right, data)
        else:
            root.left = insert_into_bst(root.left, data)
    return root


def delete_from_bst(root: BinaryTreeNode, key: int) -> BinaryTreeNode:
    if root is None:
        return root
    if key < root.data:
        root.left = delete_from_bst(root.left, key)
    elif key > root.data:
        root.right = delete_from_bst(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None  # type: ignore
            return temp
        elif root.right is None:
            temp = root.right
            root = None  # type: ignore
            return temp
        else:
            temp = find_in_bst(root.right, key)
            root.right = delete_from_bst(root.right, key)
    return root


def is_bst(root: BinaryTreeNode) -> bool:
    if root is None:
        return True
    if root.left is not None and find_max_in_bst(root.left) > root.data:
        return False
    if root.right is not None and find_min_in_bst(root.right) < root.data:
        return False
    if not is_bst(root.left) or not is_bst(root.right):
        return False
    return True


def validate_bst(root, min_value, max_value):
    if root is None:
        return True
    if root.data < min_value or root.data >= max_value:
        return False
    return validate_bst(root.left, min_value, root.data) and validate_bst(root.right, root.data, max_value)


def lca(root: BinaryTreeNode, a: int, b: int) -> BinaryTreeNode:
    if root is None:
        return root

    if root.data == a or root.data == b:
        return root

    if max(a, b) < root.data:
        return lca(root.left, a, b)
    elif min(a, b) > root.data:
        return lca(root.right, a, b)
    return root


def kth_smallest(root: BinaryTreeNode, k: int, count: int) -> BinaryTreeNode:
    if root is None:
        return root
    count = count + 1
    left = kth_smallest(root.left, k, count)
    if left is not None:
        return left
    if count == k:
        return root
    return kth_smallest(root.right, k, count)


def print_in_range(root: BinaryTreeNode, low: int, high: int) -> None:
    if root is None:
        return
    if root.data >= low:
        print_in_range(root.left, low, high)
    if low <= root.data <= high:
        print(root.data, end=' ')
    if root.data <= high:
        print_in_range(root.right, low, high)


if __name__ == '__main__':
    root = create_bst()
    TreeTraversal.in_order(root)
    result = find_in_bst(root, 7)
    print(f'\n7 exist : {result}')
    result = find_in_bst(root, 9)
    print(f'9 exist : {result}')
    result = find_in_bst(root, 11)
    print(f'11 exist : {result}')
    result = find_in_bst(root, 15)
    print(f'15 exist : {result}')

    print(f'minimum in bst : {find_min_in_bst(root)}')
    print(f'maximum in bst : {find_max_in_bst(root)}')
    insert_into_bst(root, 18)
    insert_into_bst(root, 1)
    TreeTraversal.in_order(root)
    delete_from_bst(root, 18)
    print()
    TreeTraversal.in_order(root)
    print()
    print(f'check is bst : {is_bst(root)}')
    print(f'3rd smallest number : {kth_smallest(root, 3, 1).data}')
    print_in_range(root, 4, 11)
