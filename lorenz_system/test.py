import pygame
import numpy as np
import sys

# fungsi untuk menghitung sistem Lorenz
def lorenz_system(x, y, z, s=10, r=28, b=8/3):
    x_dot = s*(y - x)
    y_dot = x*(r - z) - y
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# inisialisasi Pygame
pygame.init()

# ukuran jendela Pygame
width, height = 800, 600

# membuat jendela Pygame
screen = pygame.display.set_mode((width, height))

# membuat warna gradasi
colors = np.zeros((256, 3))
colors[:, 0] = np.linspace(0, 255, 256)
colors[:, 1] = np.linspace(0, 255, 256)
colors[:, 2] = np.linspace(255, 0, 256)

# membuat array untuk menampung posisi x, y, z
x, y, z = np.zeros(10000), np.zeros(10000), np.zeros(10000)
x[0], y[0], z[0] = 1, 1, 1

# menggambar sistem Lorenz
s = 10
r = 28
b = 8/3
dt = 0.01
for i in range(1, 10000):
    x_dot, y_dot, z_dot = lorenz_system(x[i-1], y[i-1], z[i-1], s, r, b)
    x[i] = x[i-1] + x_dot * dt
    y[i] = y[i-1] + y_dot * dt
    z[i] = z[i-1] + z_dot * dt
    
    # menggambar posisi x, y, z pada layar
    color = colors[int((z[i] - 5) / 50 * 255)]
    pygame.draw.circle(screen, color, (int(x[i]*20 + width/2), int(y[i]*20 + height/2)), 2)

# loop tak terbatas untuk menampilkan gambar terus menerus
while True:
    # pengecekan event Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # memperbarui layar Pygame
    pygame.display.update()


