import numpy as np

DEFAULT_STEP = 0.01

def trapeze(f, a, b, h):
    out = 0
    eq = f
    data = np.arange(a, b + DEFAULT_STEP, h, dtype=float)
    for i in range(1, len(data)):
        out += (eq(data[i - 1]) + eq(data[i])) * (h / 2)
    return out
