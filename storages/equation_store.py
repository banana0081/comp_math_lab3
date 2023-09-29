from numpy import sin, cos, power

storage = {
    1: {
        'equation': lambda x: x**3 - 2 * x,
        'antiderivative': lambda x: power(x, 4) / 4 - power(x, 2)
    },
    2: {
        'equation': lambda x: sin(3*x),
        'antiderivative': lambda x: -cos(3*x)/3
    },
    3: {
        'equation': lambda x: power(x, 3) - x + 4,
        'antiderivative': lambda x: power(x, 4) / 4 - power(x, 2) / 2 + 4 * x
    }
}

def getEquationById(id):
    return storage[id]['equation']

def getAntiDerivativeById(id):
    return storage[id]['antiderivative']
