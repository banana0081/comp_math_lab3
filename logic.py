import storages.equation_store as es
import storages.method_store as ms
import math_util.check_intervals as ci

def extract_equation(data):
    return data['method'], data['equation'], data['left'], data['right'], data['eps']

def integrate(data):
    method_num, eq_num, l, r, eps = extract_equation(data)
    return solution(method_num, eq_num, l, r, eps)

def solution(mn, en, l, r, eps):
    ints = ci.check(es.getEquationById(en), es.getAntiDerivativeById(en), l, r)
    res = ms.getMethodById(mn)(es.getEquationById(en), ints, eps)
    return {'answer': round(res[0], 5), 'itr': res[1]}
