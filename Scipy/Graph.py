print()
#Start Program

from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
import numpy as np

nm = np.array([[0, 1, 2],
              [1, 0, 0],
              [2, 0 , 0]])
ss = csr_matrix(nm)
print(connected_components(ss))

from scipy.sparse.csgraph import dijkstra
print(dijkstra(ss, return_predecessors= True, indices= 0))