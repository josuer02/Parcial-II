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
        """
        Inserts a new node with the given key into the AVLTree object.
        
        Args:
        key (int): The value of the new AVLNode object to be inserted into the AVLTree.
        """
        self.root = self._insert(self.root, key)    

    
    def _insert(self, node, key):
        """
        Inserts a new node with the given key into the AVLTree recursively.
        Args:
        node (AVLNode): The current AVLNode object that is being checked for insertion.
        key (int): The value of the new AVLNode object to be inserted into the AVLTree.
        Returns:
        AVLNode: The AVLNode object that was inserted into the AVLTree.
        """

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
        """
        Searches for a node with the given key in the AVLTree object.
        Args:
        key (int): The value of the AVLNode object to be searched for.
        Returns:
        AVLNode or None: If found, the AVLNode object with the given key. Otherwise, None.
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        """
        Searches for a node with the given key in the AVLTree object recursively.
        Args:
        node (AVLNode): The current AVLNode object that is being checked for the key.
        key (int): The value of the AVLNode object to be searched for.
        Returns:
        AVLNode or None: If found, the AVLNode object with the given key. Otherwise, None.
        """
        if node is None:
            print("No encontrado")
            return None

        elif node.key == key:
            print("Valor encontrado: ", node.key)
            return node

        elif node.key < key:
            return self._search(node.right, key)

        else:
            return self._search(node.left, key)
    
    def traverse(self):
        """
        Traverses the AVL tree and prints the keys in order.
        """
        self._traverse(self.root)

    def _traverse(self, node):
        """
        Helper function for traversing the AVL tree and printing the keys in order.
        Args:
            node: The node to start traversing from.
        """
        if node:
            self._traverse(node.left)
            print(node.key)
            self._traverse(node.right)

    def _height(self, node):

        """
        Calculates the height of a given node in the AVL tree.
    
        Args:
        node (AVLNode): The node for which to calculate the height.
        Returns:
        int: The height of the node, or 0 if the node is None.
        """
        if node is None:
            return 0
        else:
            return node.height

    def _balance(self, node):
        """
        Calculates the balance factor of a given node in the AVL tree.
        
        Args:
        node (AVLNode): The node for which to calculate the balance factor.
        
        Returns:
        int: The balance factor of the node, which is the difference between the heights
            of its left and right subtrees, or 0 if the node is None.
        """
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)
        
    def _rotate_right(self, node):
        """
        Performs a right rotation on a given node in the AVL tree.
        
        Args:
        node (AVLNode): The node to rotate.
        
        Returns:
        AVLNode: The new root node after the rotation.
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

    def _rotate_left(self, node):
        """
        Performs a left rotation on a given node in the AVL tree.
        
        Args:
        node (AVLNode): The node to rotate.
        
        Returns:
        AVLNode: The new root node after the rotation.
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root
    
    
    def delete(self, key):
        """
        Deletes the node with the given key from the AVL tree.
        
        Args:
        key (int): The key of the node to delete.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """
        Deletes the node with the given key from the AVL tree recursively.
        
        Args:
        node (AVLNode): The node to start the deletion from.
        key (int): The key of the node to delete.
        
        Returns:
        AVLNode: The new root node after deletion.
        """
        if node is None:
            return None

        elif key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:

            if node.left is None and node.right is None:
                node = None

            elif node.left is None:
                node = node.right

            elif node.right is None:
                node = node.left

            else:
                temp_node = self._find_min(node.right)
                node.key = temp_node.key
                node.right = self._delete(node.right, temp_node.key)

        if node is None:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance(node)

        if balance > 1 and self._balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self._balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self._balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node
    
    def _find_min(self, node):
        """
        Finds the node with the smallest key in a given subtree.
        
        Args:
        node (AVLNode): The node to start searching from.
        
        Returns:
        AVLNode: The node with the smallest key in the subtree.
        """
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node                                                                                                                         

    def find_min(self):
            if self.root is None:
                return None
            
            node = self.root
            while node.left is not None:
                node = node.left
            
            return node.key

    def find_max(self):
            if self.root is None:
                return None
            
            node = self.root
            while node.right is not None:
                node = node.right
            
            return node.key

def print_avl_tree(node, level=0, prefix=""):
        """
        Prints the AVL tree starting from the given node.
        
        Args:
        node (AVLNode): The node from which to start printing the tree.
        level (int): The level of the node in the tree (default 0).
        prefix (str): The prefix to use when printing the node (default "").
        """

        if node is not None:
            print(" " * 4 * level + prefix + str(node.key))
            print_avl_tree(node.left, level + 1, "L: ")
            print_avl_tree(node.right, level + 1, "R: ")