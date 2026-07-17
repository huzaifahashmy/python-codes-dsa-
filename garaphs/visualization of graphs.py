from graphviz import Digraph

# Node definition
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree manually
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.left.right = Node(7)

# Visualization function
def visualize(root):
    dot = Digraph()

    def add_nodes(node):
        if node:
            # create node
            dot.node(str(id(node)), str(node.val))

            # left edge
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)), label="L")
                add_nodes(node.left)

            # right edge
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)), label="R")
                add_nodes(node.right)

    add_nodes(root)
    return dot

# Generate and render
dot = visualize(root)
dot.render('binary_tree', format='png', view=True)