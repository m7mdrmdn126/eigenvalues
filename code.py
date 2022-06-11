import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la


# making a matrix to start to work on it
A = np.array([[1,0,9],[0,-2,9],[6,8,9]])

# printing the matrix 
print(" the matrix : ")
print(A)
print()

# getting the eigenvalues and eigenvectors
eigvals, eigvecs = la.eig(A)

# transposing to real numbers 
eigvals = eigvals.real

print(" eigen values ")
print(eigvals)