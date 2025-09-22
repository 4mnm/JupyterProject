import numpy as np

# Define the 2x2 arrays
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])


add_result = A + B


mul_elementwise = A * B


mat_product = A @ B   # or np.matmul(A, B)


print("A + B =\n", add_result)
print("\nElementwise multiplication (A * B) =\n", mul_elementwise)
print("\nMatrix product (A @ B) =\n", mat_product)