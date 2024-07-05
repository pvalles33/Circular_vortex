import numpy as np
import matplotlib.pyplot as plt

def generate_vortex_velocity_matrices(mesh_size, vortex_radius, max_velocity):
    x_velocity = np.zeros((mesh_size, mesh_size))
    y_velocity = np.zeros((mesh_size, mesh_size))
    
    center = mesh_size // 2  # Center of the vortex
    
    for i in range(mesh_size):
        for j in range(mesh_size):
            dx = j - center
            dy = i - center
            distance = np.sqrt(dx**2 + dy**2)
            
            if distance <= vortex_radius:
                # Angle (theta) in polar coordinates
                theta = np.arctan2(dy, dx)
                
                # Vortex velocity components
                x_velocity[i, j] = -max_velocity * (dy / vortex_radius)
                y_velocity[i, j] = max_velocity * (dx / vortex_radius)
            else:
                # Outside the vortex radius, velocity is zero
                x_velocity[i, j] = 0
                y_velocity[i, j] = 0
    
    return x_velocity, y_velocity
    
def save_velocity_matrices(x_velocity, y_velocity, x_filename, y_filename):
    # Save the x velocity component matrix to a file with tab delimiter
    np.savetxt(x_filename, x_velocity, delimiter='\t', fmt='%.6f')
    
    # Save the y velocity component matrix to a file with tab delimiter
    np.savetxt(y_filename, y_velocity, delimiter='\t', fmt='%.6f')

# Define the mesh parameters
mesh_size = 2050  # Example mesh size (11x11 cells)
vortex_radius = 1020  # Vortex radius in meters
max_velocity = 1000  # Maximum velocity in m/s

# Generate the velocity matrices
x_velocity_matrix, y_velocity_matrix = generate_vortex_velocity_matrices(mesh_size, vortex_radius, max_velocity)


# Define filenames for saving the matrices
x_filename = "x_velocity_matrix.out"  # .tsv extension to indicate tab-separated values
y_filename = "y_velocity_matrix.out"  # .tsv extension to indicate tab-separated values

# Save the matrices to files
save_velocity_matrices(x_velocity_matrix, y_velocity_matrix, x_filename, y_filename)


# Print the matrices
print("X Velocity Component Matrix:")
print(x_velocity_matrix)
print("\nY Velocity Component Matrix:")
print(y_velocity_matrix)

# Visualize the velocity field
X, Y = np.meshgrid(np.arange(mesh_size), np.arange(mesh_size))

plt.figure(figsize=(10, 10))
plt.quiver(X, Y, x_velocity_matrix, y_velocity_matrix, scale=1, scale_units='xy')
plt.xlim(0, mesh_size-1)
plt.ylim(0, mesh_size-1)
plt.gca().set_aspect('equal')
plt.title("Velocity Field of Circular Vortex")
plt.show()

