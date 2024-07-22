#!/usr/bin/env python
# coding: utf-8

# In[29]:


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
    
    rafter_length = 5000.0
    rafter_thickness = 300.0
    rafter_flange_thickness = 12.4
    rafter_web_thickness = 7.5
    rafter_angle = 30.0  # Angle in degrees for the inclination of the rafters
    
    purlin_length = 1000.0
    purlin_width = 40.0
    purlin_height = 20.0

    # Convert angle from degrees to radians
    angle_rad = np.radians(rafter_angle)

    # Create columns
    create_i_section(ax, (0, 0, 0), column_thickness, column_thickness, column_height, column_flange_thickness, column_web_thickness, 'blue')
    create_i_section(ax, (rafter_length, 0, 0), column_thickness, column_thickness, column_height, column_flange_thickness, column_web_thickness, 'blue')

    # Create inclined rafters
    rafter_length_horizontal = rafter_length * np.cos(angle_rad)
    rafter_height_vertical = rafter_length * np.sin(angle_rad)
    create_i_section(ax, (0, 0, column_height), rafter_length_horizontal, rafter_thickness, rafter_thickness, rafter_flange_thickness, rafter_web_thickness, 'green')
    create_i_section(ax, (rafter_length_horizontal, 0, column_height), -rafter_length_horizontal, rafter_thickness, rafter_thickness, rafter_flange_thickness, rafter_web_thickness, 'green')

    # Create purlins
    num_purlins = 5  # Example number of purlins
    for i in range(num_purlins):
        # Calculate purlin position along the rafter
        position_along_rafter = (i + 1) / (num_purlins + 1) * rafter_length
        purlin_x = position_along_rafter * np.cos(angle_rad)
        purlin_z = column_height + position_along_rafter * np.sin(angle_rad)
        
        # Rotate purlin 90 degrees in horizontal plane
        purlin_origin = (purlin_x - purlin_length / 2, -purlin_width / 2, purlin_z)
        plot_prism(ax, purlin_origin, purlin_length, purlin_height, purlin_width, 'red')

    # Hide the axes
    ax.set_axis_off()

    # Set the limits to ensure the entire model is visible
    ax.set_xlim([-1000, 6000])
    ax.set_ylim([-2000, 2000])
    ax.set_zlim([0, 6000])

    plt.show()

if __name__ == "__main__":
    create_portal_frame()


# In[ ]:




