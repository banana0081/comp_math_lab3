import methods.basics as base
import methods.rect as rect
import methods.trap as trap
import methods.simpsons as simp

DEFAULT_RECT_K = 2
DEFAULT_TRAPEZE_K = 2
DEFAULT_SIMPSON_K = 4

integration_methods = {
    1: lambda f, ints, eps: base.integrate(f, ints, eps, rect.left, DEFAULT_RECT_K),
    2: lambda f, ints, eps: base.integrate(f, ints, eps, rect.center, DEFAULT_RECT_K),
    3: lambda f, ints, eps: base.integrate(f, ints, eps, rect.right, DEFAULT_RECT_K),
    4: lambda f, ints, eps: base.integrate(f, ints, eps, trap.trapeze, DEFAULT_TRAPEZE_K),
    5: lambda f, ints, eps: base.integrate(f, ints, eps, simp.the_simpsons, DEFAULT_RECT_K),
}

def getMethodById(id):
    return integration_methods[id]
