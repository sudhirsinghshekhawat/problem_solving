class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def populate_nodes_to_parent(node, node_to_parent, parent=None):
    if node:
        node_to_parent[node.value] = parent
        populate_nodes_to_parent(node.left, node_to_parent, node)
        populate_nodes_to_parent(node.right, node_to_parent, node)


def get_node_from_value(node, target, node_to_parent):
    if node.value == target:
        return node
    node_parent = node_to_parent[target]
    if node_parent.left is not None and node_parent.left.value == target:
        return node_parent.left
    return node_parent.right


def bfs_distnace_k(target_node, node_to_parent, k):
    queue = [(target_node, 0)]
    seen = {target_node.value}

    while queue:
        current_node, current_distance = queue.pop(0)
        if current_distance == k:
            nodes_from_distance_k = [node.value for node, _ in queue]
            nodes_from_distance_k.append(current_node.value)
            return nodes_from_distance_k
        else:
            connect_nodes = [current_node.left, current_node.right, node_to_parent[current_node.value]]
            for node in connect_nodes:
                if node is None:
                    continue
                if node.value in seen:
                    continue
                seen.add(node.value)
                queue.append((node, current_distance + 1))
    return []


def findNodesDistanceK(tree, target, k):
    node_to_parent = {}
    populate_nodes_to_parent(tree, node_to_parent)
    target_node = get_node_from_value(tree, target, node_to_parent)
    return bfs_distnace_k(target_node, node_to_parent, k)
