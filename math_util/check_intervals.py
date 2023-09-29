import numpy as np
import warnings
warnings.filterwarnings("error")

def check(f, ader, a, b):
    step = 0.01
    correct_intervals = []

    cur_start = a
    values = np.arange(a, b, step, dtype=float)

    for i in values:
        cur = round(i, 10)
        if gap_checker(f, cur):
            convergence_checker(ader, cur)
            if cur_start == cur:
                cur_start += step
                continue
            correct_intervals.append([cur_start, cur - step])
            cur_start = cur + step

    if gap_checker(f, b):
        if cur_start < b:
            convergence_checker(ader, b)
            correct_intervals.append([cur_start, b - step])
    else:
        correct_intervals.append([cur_start, b])

    return correct_intervals

def gap_checker(equation, x):
    try:
        result = equation(x)
        if abs(result) > 1e10 or np.isinf(result):
            return True
    except Exception or RuntimeWarning:
        return True
    return False


def convergence_checker(ader, x):
    try:
        result = ader(x)
        if abs(result) > 1e10:
            raise Exception("Интеграл не существует")
    except Exception or RuntimeWarning:
        raise Exception("Интеграл не существует")
