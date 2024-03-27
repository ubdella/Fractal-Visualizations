import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(8, 8))


def newton_fractal(f, df, bounds=(-2, 2, -2, 2), max_iter=1000, density=2000):
    x_min, x_max, y_min, y_max = bounds
    x_grid = np.linspace(x_min, x_max, density)
    y_grid = np.linspace(y_min, y_max, density)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = X + 1j * Y

    def newton_step(z):
        return z - f(z) / df(z)

    fractal = np.zeros_like(Z, dtype=int)
    for i in range(density):
        for j in range(density):
            z = Z[i, j]
            for n in range(max_iter):
                z = newton_step(z)
                if abs(f(z)) < 1e-6:
                    fractal[i, j] = n
                    break

  
    extent = (x_min, x_max, y_min, y_max)
    ax.imshow(fractal, cmap='hot', extent=extent)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('Newton Fractal')


    plt.show()

# the function and its derivative
f = lambda z: z**3 - 1
df = lambda z: 3 * z**2


newton_fractal(f, df)