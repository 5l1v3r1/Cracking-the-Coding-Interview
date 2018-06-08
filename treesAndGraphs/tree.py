class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

