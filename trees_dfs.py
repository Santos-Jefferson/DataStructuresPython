class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)

    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)


n1 = Node('root node')
n2 = Node('left child node')
n3 = Node('right child node')
n4 = Node('left grandchild node')

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

# current = n1
# while current:
#     print(current.data)
#     current = current.left_child

print(n1.inorder(n1))
print()
print(n1.preorder(n1))
print()
print(n1.postorder(n1))
print()
