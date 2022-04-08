class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def overlap(l1, r1, l2, r2):
    if l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y:
        return False
    if l1.x >= r2.x or l2.x >= r1.x:
        return False
    if l1.y >= r2.y or l2.y >= r1.y:
        return False
    return True
