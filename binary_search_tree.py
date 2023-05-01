class Node:

    def __init__(self, data: int):
        """
        Initializes a new node with the given data.

        Args:
            data (int): The data to be stored in the node.
        """
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        """
        Returns a string representation of the node.

        Returns:
            str: A string representation of the node.
        """
        return '({})'.format(self.data)
    

class BinarySearchTree:

    def __init__(self):
        """
        Initializes a new binary search tree.
        """
        self.root = None


    def insert(self, value: int):
        """
        Inserts a new node with the given value into the binary search tree.

        Args:
            value (int): The value to be inserted into the tree.
        """
        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):
        """
        Recursively inserts a new node with the given value into the binary search tree.

        Args:
            value (int): The value to be inserted into the tree.
            subtree (Node): The root node of the subtree to insert the value into.
        """
        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        """
        Traverses the binary search tree and prints the values of each node in order.

        Args:
            subtree (Node): The root node of the subtree to traverse.
        """
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)


    def search(self, key: int) -> bool:
        """
        Searches for a node with the given key in the binary search tree.

        Args:
            key (int): The value to search for in the tree.

        Returns:
            bool: True if a node with the given key exists in the tree, False otherwise.
        """
        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:
        """
        Recursively searches for a node with the given key in the binary search tree.

        Args:
            key (int): The value to search for in the tree.
            subtree (Node): The root node of the subtree to search in.

        Returns:
            bool: True if a node with the given key exists in the tree, False otherwise.
        """
        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        
    def find_min(self, subtree: Node) -> int:
        """
        Finds and returns the minimum value in the subtree rooted at the given node.
        Args:
        - subtree (Node): The root node of the subtree to search.
        Returns:
        - The node with the minimum value in the subtree.
        """

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree

    def find_max(self, subtree: Node) -> int:
        """
        Finds and returns the maximum value in the subtree rooted at the given node.
        Args:
        - subtree (Node): The root node of the subtree to search.
        Returns:
        - The node with the maximum value in the subtree.
        """
        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
    
    def delete(self, value: int):
        """
        Removes the node with the given value from the tree.

        Args:
            value (int): value of the node to be removed.

        Returns:
            None.
        """
        if self.root is None:
            print('Tree is empty...')
            return
            
        else:
            self.root = self._delete(value, self.root)


    def _delete(self, value: int, node):
        """
        Private helper function that removes the node with the given key from the given subtree.

        Args:
            value (int): value of the node to be removed.
            node: Current node in the subtree.

        Returns:
            The root node of the updated subtree.
        """
        if node is None:
            print('value not found...')
            return node
            
        if value < node.data:
            node.left_child = self._delete(value, node.left_child)
            
        elif value > node.data:
            node.right_child = self._delete(value, node.right_child)
            
        else:
            if node.left_child is None:
                temp = node.right_child
                node = None
                return temp
                
            elif node.right_child is None:
                temp = node.left_child
                node = None
                return temp
                
            temp = self.find_min(node.right_child)
            node.data = temp.data
            node.right_child = self._delete(temp.data, node.right_child)
            
        return node

        
