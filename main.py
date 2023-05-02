# Espacio para realizar las pruebas
from binary_search_tree import BinarySearchTree
from avl import AVLTree, print_avl_tree
import time, matplotlib.pyplot as plt
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

#Delete
print('\n * Delete node 33***\n')
print(Avl_tree.delete(33))

print('\n * Visualize tree *\n')
print_avl_tree(Avl_tree.root)
print(Avl_tree.traverse(), "\n")

#Minimo
print('\n * Find min *\n')
print(Avl_tree.find_min())

#Maximo
print('\n * Find max *\n')
print(Avl_tree.find_max())


#AVL tree
start_time=time.time()
AVL_tree1 = AVLTree()
print('\n*** Inserting Nodes in Tree ***\n')
nodes_values = [46, 97, 12, 5, 8, 13, 43, 88, 22, 76]
for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    AVL_tree1.insert(value)
end_time=time.time()
elapsed_time=end_time-start_time
print('Tiempo transcurrido AVL', elapsed_time)

#BST tree
start_time=time.time()
BST_tree = BinarySearchTree()
print('\n*** Inserting Nodes in Tree ***\n')
nodes_values = [46, 97, 12, 5, 8, 13, 43, 88, 22, 76]
for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    BST_tree.insert(value)
end_time=time.time()
elapsed_time=end_time-start_time
print('Tiempo transcurrido BST', elapsed_time)

busqueda = [46, 97, 12, 88, 22, 43, 8, 5, 12, 76, 46, 97, 12, 88, 22, 43, 8, 5, 12, 76]
times1 = []
times2 = []
elapsed_time1=0
elapsed_time2=0
for i in busqueda:
    # Medir el tiempo de ejecución de la primera implementación
    start_time = time.time()
    AVL_tree1.search(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time1=elapsed_time1+elapsed_time
    times1.append(elapsed_time1)
    
    # Medir el tiempo de ejecución de la segunda implementación
    start_time = time.time()
    BST_tree.search(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time2=elapsed_time2+elapsed_time
    times2.append(elapsed_time2)


print('Tiempo transcurrido AVL search: ', elapsed_time1)
print('Tiempo transcurrido BST search: ', elapsed_time2)

# Graficar los resultados
plt.plot( times1, label="AVL")
plt.plot( times2, label="BST")
plt.xlabel("Iteración")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.show()