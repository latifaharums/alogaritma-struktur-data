#BINARY SEARCH TREE YANG ADA FITUR SEARCHING

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data:
            return self.left.search(data) if self.left else None
        else:
            return self.right.search(data) if self.right else None
    def show(self, level=0, prefix='-'):
        print('  ' * level, prefix, self.data)
        if self.left: self.left.show(level + 1, '<')
        if self.right: self.right.show(level + 1, '>')

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)
    def search(self, data):
        return self.root.search(data)
    def show(self):
        self.root.show()

tree = BinarySearchTree()
tree.add(5)
tree.add(2)
tree.add(8)
tree.add(1)
tree.add(3)
tree.add(6)
tree.add(9)
node = tree.search(4)
if node:
    node.show()
else:
    print('tidak ketemu')