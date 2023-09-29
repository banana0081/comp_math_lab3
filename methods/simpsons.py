import numpy as np

DEFAULT_STEP = 0.01

def the_simpsons(f, a, b, h):
    out = 0
    data = np.arange(a, b + DEFAULT_STEP, h, dtype=float)
    out += f(data[0]) + f(data[len(data)-1])
    for i in range(1, len(data)-1, 2):
        out += 4 * f(data[i])
    for i in range(2, len(data) - 2, 2):
        out += 2 * f(data[i])
    return out * h / 3
