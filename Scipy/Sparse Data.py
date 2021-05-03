print()
#Start Program

from scipy.sparse import csr_matrix
import numpy as np

arr = np.array([[0, 0, 0],[1 , 0 , 2], [1, 0, 0]])
print(csr_matrix(arr).data)
mtc = csr_matrix(arr).tocsc();
print(mtc)