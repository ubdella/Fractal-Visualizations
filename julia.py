import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(8, 8))

def julia(z, c, max_iter=70):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

# complex constant c for the Julia set
c = -0.8 + 0.156j

# a grid of complex numbers
x_min, x_max = -2, 2
y_min, y_max = -2, 2
x_grid = np.linspace(x_min, x_max, 1000)
y_grid = np.linspace(y_min, y_max, 1000)
X, Y = np.meshgrid(x_grid, y_grid)
Z = X + 1j * Y


julia_set = np.zeros_like(Z, dtype=int)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        julia_set[i, j] = julia(Z[i, j], c)


ax.imshow(julia_set, cmap='hot', extent=(x_min, x_max, y_min, y_max))
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_title(f'Julia Set for c={c:.3f}')

plt.show()