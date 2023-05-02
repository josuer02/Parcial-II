# Espacio para realizar las pruebas
from binary_search_tree import BinarySearchTree
from avl import AVLTree, print_avl_tree
import time, matplotlib.pyplot as plt
import random,sys

Avl_tree = AVLTree()

#AVL tree
start_time=time.time()
AVL_tree1 = AVLTree()
print('\n*** Inserting Nodes in Tree ***\n')
nodes_values1 = set(random.sample(range(1, 10001), 10000))
for value in nodes_values1:
    print('Inserting node with value: {}'.format(value))
    AVL_tree1.insert(value)
end_time=time.time()
elapsed_time=end_time-start_time
print('Tiempo transcurrido AVL', elapsed_time)
size=sys.getsizeof(AVL_tree1)
print(f"Tamaño del objeto tree: {size:.2f} Bytes")

#BST tree
start_time=time.time()
BST_tree = BinarySearchTree()
print('\n*** Inserting Nodes in Tree ***\n')
nodes_values = nodes_values1.copy()
for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    sys.setrecursionlimit(10000000)
    BST_tree.insert(value)
end_time=time.time()
elapsed_time=end_time-start_time
print('Tiempo transcurrido BST', elapsed_time)

times1 = []
times2 = []
elapsed_time1=0
elapsed_time2=0
for i in range(10001):
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