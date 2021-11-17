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
#fives_array = np.full(10,7)
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

## Additional numpy classwork

# create array of 25 random numbers
rand_array = np.random.randn(25)
print(rand_array)

# 10x10 matrix 0 to 1
#matrix_ten_by_ten = np.linspace(0,1,100).reshape(10,10)
matrix_ten_by_ten = np.arange(1,101).reshape(10,10) / 100
print(matrix_ten_by_ten)

# array of 20 linearly spaced points between 0 and 1
array_linear_spaced = np.linspace(0,1,20)
print(array_linear_spaced)

# splice given matrix according to given instructions
original_matrix = np.arange(1,26).reshape(5,5)
print(original_matrix)

# select rows 3 onwards, columns 2 onwards
matrix_splice_one = original_matrix[2:,1:]
print(matrix_splice_one)

# select entry at (4,5)
matrix_splice_two = original_matrix[3,4]
print(matrix_splice_two)

# select rows after 3, column 2 as unique rows
matrix_splice_three = original_matrix[:3,1:2]
print(matrix_splice_three)

# select all from row 5
matrix_splice_four = original_matrix[4,:]
print(matrix_splice_four)

# select all from rows 4 to 5
matrix_splice_five = original_matrix[3:5,:]
print(matrix_splice_five)

# sum values in given matrix
matrix_sum = original_matrix.sum()
print(matrix_sum)

# get std dev of values in given matrix
matrix_std_dev = original_matrix.std()
print(matrix_std_dev)

# get sum of columns in given matrix
column_sum = original_matrix.sum(axis=0)
print(column_sum)

# get sum of rows in given matrix
row_sum = original_matrix.sum(axis=1)
print(row_sum)