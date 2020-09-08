class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


def breadth_first_traversal(root_node):
    # Empty list (queue) to add and remove nodes
    deque = []
    # Empty list to add the nodes for final result
    list_of_nodes = []
    # Add the root node to the queue(list)
    deque.append(root_node)

    while len(deque) > 0:
        # Assign to a variable and remove it
        node = deque.pop(0)
        # Add to the result and final list
        list_of_nodes.append(node.data)
        if node.left_child:  # if left_child exist
            # Append to the queue (list)
            deque.append(node.left_child)
        if node.right_child:  # if right_child exist
            # Append to the queue (list)
            deque.append(node.right_child)
    return list_of_nodes

print(breadth_first_traversal(n1))
