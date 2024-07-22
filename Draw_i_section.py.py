#!/usr/bin/env python
# coding: utf-8

# In[38]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_prism(ax, origin, length, width, height, color):
    """Plots a rectangular prism given an origin point, length, width, height, and color."""
    x, y, z = origin
    vertices = [
        [x, y, z], [x + length, y, z], [x + length, y + width, z], [x, y + width, z], 
        [x, y, z + height], [x + length, y, z + height], [x + length, y + width, z + height], [x, y + width, z + height]
    ]
    verts = [[vertices[j] for j in [0, 1, 5, 4]], [vertices[j] for j in [1, 2, 6, 5]], [vertices[j] for j in [2, 3, 7, 6]], 
             [vertices[j] for j in [3, 0, 4, 7]], [vertices[j] for j in [0, 1, 2, 3]], [vertices[j] for j in [4, 5, 6, 7]]]
    ax.add_collection3d(Poly3DCollection(verts, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))

def create_i_section(ax, origin, length, width, height, flange_thickness, web_thickness, color):
    """Creates an I-section and adds it to the plot."""
    x, y, z = origin
    # Bottom flange
    plot_prism(ax, (x, y, z), length, width, flange_thickness, color)
    # Top flange
    plot_prism(ax, (x, y, z + height - flange_thickness), length, width, flange_thickness, color)
    # Web
    plot_prism(ax, (x, y + (width - web_thickness) / 2, z + flange_thickness), length, web_thickness, height - 2 * flange_thickness, color)

def create_portal_frame():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the dimensions
    column_height = 4000.0
    column_thickness = 400.0
    column_flange_thickness = 12.70
    column_web_thickness = 9.10
    
    rafter_length = 3000.0  # Horizontal projection of the rafter
    rafter_thickness = 300.0
    rafter_flange_thickness = 12.4
    rafter_web_thickness = 7.5
    rafter_angle = 60.0  # Angle between the rafters in degrees
    
    purlin_length = 1000.0
    purlin_width = 40.0
    purlin_height = 20.0
    
    # Calculate the height at which the rafters meet
    rafter_meet_height = column_height + rafter_length * np.tan(np.radians(rafter_angle / 2))

    # Create columns
    create_i_section(ax, (0, 0, 0), column_thickness, column_thickness, column_height, column_flange_thickness, column_web_thickness, 'blue')
    create_i_section(ax, (rafter_length * 2, 0, 0), column_thickness, column_thickness, column_height, column_flange_thickness, column_web_thickness, 'blue')

    # Create inclined rafters
    # Left rafter
    create_i_section(ax, (0, 0, column_height), rafter_length, rafter_thickness, rafter_thickness, rafter_flange_thickness, rafter_web_thickness, 'green')
    # Right rafter
    create_i_section(ax, (rafter_length, 0, column_height), rafter_length, rafter_thickness, rafter_thickness, rafter_flange_thickness, rafter_web_thickness, 'green')
    
    # Position rafters correctly
    rafter_left_origin = (0, 0, column_height)
    rafter_right_origin = (rafter_length * 2, 0, column_height)

    ax.plot([rafter_left_origin[0], rafter_length], [rafter_left_origin[1], 0], [rafter_left_origin[2], rafter_meet_height], color='green')
    ax.plot([rafter_right_origin[0], rafter_length], [rafter_right_origin[1], 0], [rafter_right_origin[2], rafter_meet_height], color='green')
    
    # Create purlins
    num_purlins = 5  # Example number of purlins
    for i in range(num_purlins):
        purlin_y = (i * 150.0) - ((num_purlins / 2) * 150.0)
        purlin_z = column_height + (rafter_length / num_purlins) * i * np.tan(np.radians(rafter_angle / 2))
        # Purlins along left rafter
        purlin_origin_left = (rafter_length / num_purlins * i, purlin_y, purlin_z)
        plot_prism(ax, purlin_origin_left, purlin_length, purlin_width, purlin_height, 'red')
        # Purlins along right rafter
        purlin_origin_right = (rafter_length + rafter_length / num_purlins * i, purlin_y, purlin_z)
        plot_prism(ax, purlin_origin_right, purlin_length, purlin_width, purlin_height, 'red')

    # Hide the axes
    ax.set_axis_off()

    # Set the limits to ensure the entire model is visible
    ax.set_xlim([-1000, 6000])
    ax.set_ylim([-2000, 6000])
    ax.set_zlim([0, 6000])

    plt.show()

if __name__ == "__main__":
    create_portal_frame()


# In[ ]:




