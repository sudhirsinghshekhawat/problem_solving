import sys
from builtins import max
from collections import deque

from trees.BinaryTree import BinaryTreeNode


def create_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    return root


def find_max_in_bt(root):
    max_val = -sys.maxsize - 1
    if root:
        left_max = find_max_in_bt(root.left)
        right_max = find_max_in_bt(root.right)
        if left_max > right_max:
            max_val = left_max
        else:
            max_val = right_max

        if root.data > max_val:
            max_val = root.data
    return max_val


def search_in_bt(root, data):
    if root:
        if root.data == data:
            return True
        return search_in_bt(root.left, data) or search_in_bt(root.right, data)
    return False


def max_depth(root):
    if root:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)

        if left_depth > right_depth:
            return 1 + left_depth
        else:
            return 1 + right_depth
    return 0


def height_of_tree(root):
    if root is None:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    return 1 + max(left_height, right_height)


def diameter(root):
    if root is None:
        return 0

    lheight = height_of_tree(root.left)
    rheight = height_of_tree(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)
    return max(1 + lheight + rheight, max(left_diameter, right_diameter))


def reverse_level_order(root):
    if root is None:
        return
    q = deque()
    reverse_order = deque()
    q.append(root)
    while q:
        tmp = q.popleft()
        reverse_order.append(tmp.data)
        if tmp.right:
            q.append(tmp.right)
        if tmp.left:
            q.append(tmp.left)
    while reverse_order:
        print(reverse_order.pop(), end=' ')


def get_max_width_of_binary_tree(root):
    max_width = 0
    h = height_of_tree(root) + 1
    for i in range(1, h + 1):
        width = get_width(root, i)
        if width > max_width:
            max_width = width
    return max_width


def get_width(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level >= 1:
        return get_width(root.left, level - 1) \
               + get_width(root.right, level - 1)


def width_bt(root):
    if not root:
        return 0
    max_width = 0
    queue = deque()
    queue.append((root, 0))

    while queue:
        level_length = len(queue)
        _, level_head_index = queue[0]

        for _ in range(level_length):
            node, col_index = queue.popleft()
            if node.left:
                queue.append((node.left, col_index * 2 + 1))
            if node.right:
                queue.append((node.right, col_index * 2 + 2))
        max_width = max(max_width, col_index - level_head_index + 1)

    return max_width


def max_sum_at_level(root):
    if root is None:
        return 0
    q = deque()
    q.append(root)
    q.append(None)
    max_sum = -sys.maxsize - 1
    curr_sum = 0

    while q:
        tmp = q.popleft()
        if tmp:
            curr_sum = curr_sum + tmp.data
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        else:
            if q:
                q.append(None)
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr_sum = 0
    return max_sum


def print_path(root):
    path = []
    print_all_path_root_leaf(root, path, 0)


def print_all_path_root_leaf(root, path, path_len):
    if root is None:
        return
    if len(path) > path_len:
        path[path_len] = root.data
    else:
        path.append(root.data)

    path_len = path_len + 1

    if root.left is None and root.right is None:
        printArray(path, path_len)
    else:
        print_all_path_root_leaf(root.left, path, path_len)
        print_all_path_root_leaf(root.right, path, path_len)


def printArray(ints, len):
    for i in ints[0: len]:
        print(i, " ", end="")
    print()


def print_zig_zag_traversal(root):
    if root is None:
        return []
    zig_zag_arr = []
    q = deque()
    s = deque()
    ltor = True
    q.append(root)
    q.append(None)
    tmp_arr = []

    while q:
        tmp = q.popleft()
        if tmp:
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
            tmp_arr.append(tmp.data)
        else:
            if q:
                q.append(None)
            if ltor:
                zig_zag_arr.extend(tmp_arr)
            else:
                for val in tmp_arr:
                    s.append(val)
                while s:
                    val = s.pop()
                    print(val)
                    zig_zag_arr.append(val)
            tmp_arr = []
            ltor = not ltor

    print(zig_zag_arr)


def vertical_sum_uti(root, hd, map):
    if root is None:
        return
    vertical_sum_uti(root.left, hd - 1, map)
    if hd in map.keys():
        map[hd] = map[hd] + root.data
    else:
        map[hd] = root.data
    vertical_sum_uti(root.right, hd + 1, map)


def vertical_sum(root):
    map = {}
    vertical_sum_uti(root, 0, map)

    print(map)


def find_num_of_unique_tree(n):
    return pow(2, n) - n


def diagnol(root):
    out = []
    if root:
        node = root
    left_q = deque()
    while node:
        out.append(node.data)
        if node.left:
            left_q.append(node.left)
        if node.right:
            node = node.right
        else:
            if len(left_q) >= 1:
                node = left_q.popleft()
            else:
                node = None
    return out


def diagonal_recursive(root, d, printMap):
    if root is None:
        return
    try:
        printMap[d].append(root.data)
    except KeyError:
        printMap[d] = root.data
    diagonal_recursive(root.left, d + 1, printMap)
    diagonal_recursive(root.right, d, printMap)


def min_depth_bst(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None and root.right is not None:
        return 1 + min_depth_bst(root.right)

    if root.right is None and root.left is not None:
        return 1 + min_depth_bst(root.left)

    return 1 + min(min_depth_bst(root.left), min_depth_bst(root.right))


if __name__ == '__main__':
    root = create_tree()
    max_ = find_max_in_bt(root)
    print(f'maximum value in tree is : {max_}')
    result = search_in_bt(root, 6)
    print(result)
    result = search_in_bt(root, 13)
    print(result)

    depth = max_depth(root)
    print(f'max depth : {depth}')

    height = height_of_tree(root)
    print(f'height of tree : {height}')

    diameter_of_tree = diameter(root)
    print(f'diameter of tree : {diameter_of_tree}')
    reverse_level_order(root)

    print(f'\nmax width of tree : {get_max_width_of_binary_tree(root)}')

    print(f'max sum at level : {max_sum_at_level(root)}')

    print_path(root)
    print_zig_zag_traversal(root)

    vertical_sum(root)

    print(diagnol(root))

    printMap = dict()  # type:ignore
    diagonal_recursive(root, 0, printMap)
    print(printMap)
