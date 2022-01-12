class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def appendChild(self, data):
        node = TreeNode(data)
        self.children.append(node)
    def show(self, level=0):
        print(('  ' * level), f'<{self.data}>')
        for child in self.children:
            child.show(level + 1)
        print(('  ' * level), f'</{self.data}>')

class Tree:
    def __init__(self, root=None):
        self.root = root
    def show(self):
        self.root.show()

'''
tree = Tree()
tree.root = TreeNode(4)
'''
tree = Tree(TreeNode('html'))
tree.root.appendChild('head')
tree.root.appendChild('body')
tree.root.children[0].appendChild('meta')
tree.root.children[0].appendChild('title')
tree.root.children[1].appendChild('h1')
tree.root.children[1].appendChild('ol')
tree.root.children[1].children[1].appendChild('li')
tree.root.children[1].children[1].appendChild('li')
tree.show()