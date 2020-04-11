import matplotlib.pyplot as plt
import numpy as np
import time


def get_stability(c, max_iterations=100): 
    """
    Calculate z_{n+1} = z_{n}**2 + c and return the number of iterations until abs(z) > 2
    """
    z = 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return i


def calc_mb_set(xlim=[-2.5, 1.5], ylim=[-1.5, 1.5], N=None, max_iterations=100):
    """
    Calculate the entire mandelbrot set within xlim and ylim. Return the set
    in an ndarray.
    """

    if not N:
        nx, ny=600, 600
    elif len(N)==1:
        nx, ny = N, N
    elif len(N)==2:
        nx, ny = N[0], N[1]

    xlim = sorted(xlim)
    ylim = sorted(ylim)
    x = np.linspace(xlim[0], xlim[1], nx)
    y = np.linspace(ylim[0], ylim[1], ny)
    
    mb_set = np.zeros((len(y), len(x)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            mb_set[j,i] = get_stability(c, max_iterations)

    return mb_set

def plot_mb_set(mb_set, xlim=[-2.5, 1.5], ylim=[-1.5, 1.5]):

    fig = plt.figure()

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    
    cmap = ['RdGy', 'seismic', 'jet', 'cividis', 'inferno', 'plasma', 'binary', 'PuBu', 'Blues', 'Greys']
    im = plt.imshow(mb_set, cmap=cmap[1], interpolation='bilinear', origin='lower', extent=[xlim[0], xlim[1], ylim[0], ylim[1]])
    plt.tight_layout()

    return im, cmap




if __name__ == '__main__':

    # Enable interactive plotting
    plt.ion()

    mb_set = calc_mb_set()
    im, cmap = plot_mb_set(mb_set)