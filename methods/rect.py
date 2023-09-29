import numpy as np
DEFAULT_STEP = 0.01

def integrate_rect(f, a, b, h):
    return sum(f(np.arange(a, b, h, dtype=float))) * h

def right(f, a, b, h):
    return integrate_rect(f, a + h, b + DEFAULT_STEP, h)

def left(f, a, b, h):
    return integrate_rect(f, a, b, h)

def center(f, a, b, h):
    return integrate_rect(f, a + h / 2, b - h / 2, h)
