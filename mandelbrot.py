import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))


def mandelbrot(c, max_iter=70):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

# a grid of complex numbers
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
x_grid = np.linspace(x_min, x_max, 1000)
y_grid = np.linspace(y_min, y_max, 1000)
X, Y = np.meshgrid(x_grid, y_grid)
C = X + 1j * Y


mandel = np.zeros_like(C, dtype=int)
for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        mandel[i, j] = mandelbrot(C[i, j])


ax.imshow(mandel, cmap='hot', extent=(x_min, x_max, y_min, y_max))
ax.set_xlabel('Re(c)')
ax.set_ylabel('Im(c)')
ax.set_title('Mandelbrot Set')

plt.show()