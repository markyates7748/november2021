## Coding Exercise 1:

# 1: Import np
import numpy as np

# 2: Array of 10 zeros
zeros_array = np.zeros(10)
print(zeros_array)

# 3: Array of 10 ones
ones_array = np.ones(10)
print(ones_array)

# 4: Array of 10 fives
fives_array = np.ones(10) * 5
print(fives_array)

# 5: Array of int from 10 to 50
int_array = np.arange(10,51)
print(int_array)

# 6: Array of even int from 10 to 50
even_int_array = np.arange(10,51,2)
print(even_int_array)

# 7: 3x3 matrix with values 0-8
int_matrix = np.arange(9).reshape(3,3)
print(int_matrix)

# 8: 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# 9: Generate random number between 0 and 1
rand_val = np.random.rand(1)
print(rand_val)
