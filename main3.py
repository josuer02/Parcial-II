# Espacio para realizar las pruebas
from binary_search_tree import BinarySearchTree
from avl import AVLTree, print_avl_tree
Avl_tree = AVLTree()
import random

N=100
nodes_values = random.sample(range(1, 101), N)
for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    Avl_tree.insert(value)


#Visualizer
print('\n * Visualize tree *\n')
print_avl_tree(Avl_tree.root)