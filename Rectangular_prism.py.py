#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_prism(ax, length, breadth, height, color):
    """Plots a rectangular prism given length, breadth, height, and color."""
    # Define the vertices of the prism
    vertices = np.array([
        [0, 0, 0], [length, 0, 0], [length, breadth, 0], [0, breadth, 0],  # Bottom face
        [0, 0, height], [length, 0, height], [length, breadth, height], [0, breadth, height]  # Top face
    ])
    
    # Define the 6 faces of the prism
    faces = [
        [vertices[j] for j in [0, 1, 5, 4]],  # Front face
        [vertices[j] for j in [1, 2, 6, 5]],  # Right face
        [vertices[j] for j in [2, 3, 7, 6]],  # Back face
        [vertices[j] for j in [3, 0, 4, 7]],  # Left face
        [vertices[j] for j in [0, 1, 2, 3]],  # Bottom face
        [vertices[j] for j in [4, 5, 6, 7]]   # Top face
    ]
    
    # Add faces to the plot
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))

def display_prism(length, breadth, height):
    """Creates and displays a 3D rectangular prism."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the rectangular prism
    plot_prism(ax, length, breadth, height, 'green')
    
    # Set the aspect ratio to be equal
    ax.set_aspect('auto')
    
    # Set the limits
    ax.set_xlim([0, length])
    ax.set_ylim([0, breadth])
    ax.set_zlim([0, height])
    
    # Hide the axes
    ax.set_axis_off()
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Dimensions of the rectangular prism
    length = 40.0
    breadth = 20.0
    height = 100.0

    # Display the rectangular prism
    display_prism(length, breadth, height)


# In[ ]:




