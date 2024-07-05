import numpy as np
import matplotlib.pyplot as plt

def generate_z_matrix(mesh_size, vortex_radius, max_velocity):
    z = np.zeros((mesh_size, mesh_size))
    return z
    
def save_z_matrix(z, x_filename):
    # Save the x velocity component matrix to a file with tab delimiter
    np.savetxt(x_filename, z, delimiter='\t', fmt='%.6f')

# Define the mesh parameters
mesh_size = 2050  # Example mesh size (11x11 cells)
vortex_radius = 1020  # Vortex radius in meters
max_velocity = 0  # Maximum velocity in m/s

# Generate the velocity matrices
z = generate_z_matrix(mesh_size, vortex_radius, max_velocity)


# Define filenames for saving the matrices
x_filename = "dem.input"  # .tsv extension to indicate tab-separated values

# Save the matrices to files
save_z_matrix(z, x_filename)


