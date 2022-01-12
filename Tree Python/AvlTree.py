class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.bf = 0
    def add(self, data):
        node = Node(data)
        self.add_node(node)
    def add_node(self, node):
        if node.data < self.data:
            self.bf += 1
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.add_node(node)
        else:
            self.bf -= 1
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.add_node(node)
    def left_rotate(self):
        if self.right is None:
            return
        if self.parent is not None:
            if self.data < self.parent.data:
                self.parent.left = self.right
            else:
                self.parent.right = self.right
        tmp = self.right
        self.right = self.right.left
        tmp.left = self
        self.bf += 1
        tmp.bf += 1
        return tmp
    def right_rotate(self):
        if self.left is None:
            return
        if self.parent is not None:
            if self.data < self.parent.data:
                self.parent.left = self.left
            else:
                self.parent.right = self.left
        tmp = self.left
        self.left = self.left.right
        tmp.right = self
        self.bf -= 1
        tmp.bf -= 1
        return tmp
    def show(self, level=0, prefix='-'):
        print('  ' * level, prefix, self.data)
        if self.left: self.left.show(level + 1, '<')
        if self.right: self.right.show(level + 1, '>')

class AVLTree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)
    def show(self):
        self.root.show()

tree = AVLTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.show()
tree.root = tree.root.left_rotate()
tree.show()