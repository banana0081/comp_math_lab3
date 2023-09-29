DEFAULT_N = 4
DEFAULT_STEP = 0.01

def integrate(f, intervals, eps, integral_type, k):
    diff = eps
    it = 0
    last = 1e10
    n = DEFAULT_N / 2
    result = 0
    while eps <= diff and it < 500:
        result = 0
        n *= 2
        for cur in intervals:
            h = (cur[1] - cur[0]) / n
            result += integral_type(f, cur[0], cur[1], h)
        diff = abs(last - result) / (pow(2, k) - 1)
        last = result
        it += 1
    return [result, n]