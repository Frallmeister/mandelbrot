import matplotlib.pyplot as plt
import numpy as np
import time

t0 = time.time()
x_min, x_max = -2.2, -0.6
y_min, y_max = -0.5, 0.5
N = 10**4

max_iterations=100

def mandelbrot(c, max_iterations): 
    z = 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return i

x = np.linspace(x_min, x_max, N)
y = np.linspace(y_min, y_max, N)

mb = np.zeros((len(y), len(x)))
for i in range(len(x)):
    for j in range(len(y)):
        c = complex(x[i], y[j])
        mb[j,i] = mandelbrot(c, max_iterations)

plt.imshow(mb, cmap='gnuplot2', interpolation='bilinear', origin='lower', extent=[x_min, x_max, y_min, y_max])

print(N, time.time()-t0)
plt.show()