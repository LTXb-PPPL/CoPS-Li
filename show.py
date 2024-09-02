
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def patch(ax, x, y, z, v, vmin=0, vmax=100, cmap_name='viridis'):
    cmap = mpl.cm.get_cmap(cmap_name)               # Get colormap by name
    c = cmap(mpl.colors.Normalize(vmin, vmax)(v))   # Normalize value and get color
    pc = Poly3DCollection([list(zip(x,y,z))])       # Create PolyCollection from coords
    pc.set_facecolor(c)                             # Set facecolor to mapped value
    #pc.set_edgecolor(c)
    # Set edgecolor to black
    pc.set_alpha(0.5)                               # Set transparency
    ax.add_collection3d(pc)                         # Add PolyCollection to axes
    return pc

def patch_inactive(ax, x, y, z):
    pc = Poly3DCollection([list(zip(x,y,z))])       # Create PolyCollection from coords
    pc.set_facecolor('black')                             # Set facecolor to mapped value
    #pc.set_edgecolor()
    # Set edgecolor to black
    pc.set_alpha(0.15)                               # Set transparency
    ax.add_collection3d(pc)                         # Add PolyCollection to axes
    return pc

def set_axes_equal(ax):
    """
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    """

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
    return