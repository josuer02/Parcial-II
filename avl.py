
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))

        balance = self._balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None

        elif node.key == key:
            print("Valor encontrado: ", node.key)
            return node

        elif node.key < key:
            return self._search(node.right, key)

        else:
            return self._search(node.left, key)
    
    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, node):
        if node:
            self._traverse(node.left)
            print(node.key)
            self._traverse(node.right)

    def _height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def _balance(self, node):
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)
    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

def print_avl_tree(node, level=0, prefix=""):
        if node is not None:
            print(" " * 4 * level + prefix + str(node.key))
            print_avl_tree(node.left, level + 1, "L: ")
            print_avl_tree(node.right, level + 1, "R: ")
