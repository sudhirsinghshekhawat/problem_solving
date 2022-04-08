class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeTraversal:

    @staticmethod
    def pre_order(root: BinaryTreeNode):
        if root:
            print(root.data, end=' ')
            TreeTraversal.pre_order(root.left)
            TreeTraversal.pre_order(root.right)

    @staticmethod
    def in_order(root: BinaryTreeNode):
        if root:
            TreeTraversal.in_order(root.left)
            print(root.data, end=' ')
            TreeTraversal.in_order(root.right)

    @staticmethod
    def post_order(root: BinaryTreeNode):
        if root:
            TreeTraversal.post_order(root.left)
            TreeTraversal.post_order(root.right)
            print(root.data, end=' ')


class TreeTraversalWithoutRecursion:

    @staticmethod
    def pre_order(root: BinaryTreeNode):
        list = []
        traversal_list = []
        list.append(root)
        while list:
            temp = list.pop()
            if temp.right:
                list.append(temp.right)
            if temp.left:
                list.append(temp.left)
            traversal_list.append(temp.data)
        return traversal_list

    @staticmethod
    def in_order(root: BinaryTreeNode):
        list = []
        traversal_list = []
        done = False
        curr = root

        while not done:
            if curr:
                list.append(curr)
                curr = curr.left
            else:
                if not list:
                    done = True
                else:
                    curr = list.pop()
                    traversal_list.append(curr.data)
                    curr = curr.right
        return traversal_list

    @staticmethod
    def post_order(root):
        list = []
        traversal_list = []
        list.append(root)
        prev = None
        while list:
            curr = list[-1]
            if prev is None or prev.left == curr or prev.right == curr:
                if curr.left:
                    list.append(curr.left)
                else:
                    if curr.right:
                        list.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    list.append(curr.right)
            else:
                traversal_list.append(curr.data)
                list.pop()
            prev = curr
        return traversal_list

    @staticmethod
    def level_order(root):
        list = []
        traversal_list = []
        list.append(root)

        while list:
            temp = list.pop()
            traversal_list.append(temp.data)
            if temp.left:
                list.insert(0, temp.left)
            if temp.right:
                list.insert(0, temp.right)
        return traversal_list


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    print("Recursive way")
    print("Pre Order : ", end=' ')
    TreeTraversal.pre_order(root)

    print("\nIn Order : ", end=' ')
    TreeTraversal.in_order(root)

    print("\nPost Order : ", end=' ')
    TreeTraversal.post_order(root)

    print("\nNon Recursive way")

    traversal_list = TreeTraversalWithoutRecursion.pre_order(root)
    print(f"Pre Order : {traversal_list}")

    traversal_list = TreeTraversalWithoutRecursion.in_order(root)
    print(f"In Order : {traversal_list}")

    traversal_list = TreeTraversalWithoutRecursion.post_order(root)
    print(f"Post order  : {traversal_list}")

    traversal_list = TreeTraversalWithoutRecursion.level_order(root)
    print(f"Level order  : {traversal_list}")
