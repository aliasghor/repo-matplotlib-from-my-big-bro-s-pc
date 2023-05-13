import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interact, fixed

# fungsi untuk menghitung sistem Lorenz
def lorenz_system(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# fungsi untuk menggambar plot 3D Lorenz system
def plot_lorenz(xyz, dt=0.01, s=10, r=28, b=2.667):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))
    ax.set_axis_off()
    
    x, y, z = xyz[:, 0], xyz[:, 1], xyz[:, 2]
    for i in range(len(x) - 1):
        x_dot, y_dot, z_dot = lorenz_system(x[i], y[i], z[i], s=s, r=r, b=b)
        x[i+1] = x[i] + (x_dot * dt)
        y[i+1] = y[i] + (y_dot * dt)
        z[i+1] = z[i] + (z_dot * dt)
    ax.plot(x, y, z, color='orange')
    plt.show()

# membuat titik awal
np.random.seed(1)
x0 = -15 + 30*np.random.random(3)
x, y, z = [np.zeros(10000) for i in range(3)]
x[0], y[0], z[0] = x0[0], x0[1], x0[2]

xyz = np.column_stack((x, y, z))

# menampilkan plot 3D interaktif
interact(plot_lorenz, xyz=fixed(xyz), dt=(0.01, 0.5, 0.01), s=(0, 50, 1), r=(0, 50, 1), b=(0, 8/3, 0.01))
