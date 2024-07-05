import numpy as np

def read_matrix(filename):
    # Read the matrix from the file with tab as delimiter
    matrix = np.loadtxt(filename, delimiter='\t')
    return matrix

def reverse_rows(matrix):
    # Reverse the order of the rows
    reversed_matrix = matrix[::-1]
    return reversed_matrix

def write_matrix(matrix, filename):
    # Write the matrix to a file with tab as delimiter and 6 decimal places
    np.savetxt(filename, matrix, delimiter='\t', fmt='%.6f')

# Define filenames for reading and writing
input_filename = 'y_velocity_matrix.out'
output_filename = 'vini.input'

# Read the original matrix
original_matrix = read_matrix(input_filename)

# Reverse the rows of the matrix
reversed_matrix = reverse_rows(original_matrix)

# Write the new matrix to a file
write_matrix(reversed_matrix, output_filename)

print(f"Original matrix read from {input_filename}")
print(f"New matrix with reversed rows written to {output_filename}")

