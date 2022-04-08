def findClosetValueHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if target < tree.value:
        return findClosetValueHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosetValueHelper(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBst(tree, target):
    return findClosetValueHelper(tree, target, tree.value)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
