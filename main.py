# Espacio para realizar las pruebas
from binary_search_tree import BinarySearchTree
from avl import AVLTree, print_avl_tree

Avl_tree = AVLTree()

#Funcion de insertar
print('\n*** Inserting Nodes in Tree ***\n')
nodes_values = [33, 77, 4, 11, 16, 55, 5, 1, 14, 63]
for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    Avl_tree.insert(value)

print('Current root: {}'.format(Avl_tree.root)) # current root


# Funcion de buscar
print('\n*** Searching keys in Tree ***\n')
Avl_tree.search(10)

# Funcion de traverse
print('\n*** Traversing Tree ***\n')

print(Avl_tree.traverse(), "\n")

#Visualizer
print('\n *** Visualize tree ***\n')
print_avl_tree(Avl_tree.root)