import numpy as np

A=np.array([
    [1,2,5],
    [3,7,2],
    [9,7,4]
])
print("A\n",A)
print("Determinant of A\n",np.linalg.det(A))
print("Inverse of A\n",np.linalg.inv(A))
eigenvalues, eigenvector = np.linalg.eig(A)
print("Eigen values\n",eigenvalues)
print("Eigen vector\n",eigenvector)

U, S, Vt = np.linalg.svd(A)
print("Left singular vector\n",U)
print("Diagonal Matrix\n",S)
print("Right singular vector\n",Vt)

sigma=np.zeros((3,3))
np.fill_diagonal(sigma,S)
reconstructed_matrix=U@sigma@Vt
print("Original Matrix\n",reconstructed_matrix)
