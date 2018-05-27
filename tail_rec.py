import types
import dis


def tramp(gen, *args, **kwargs):
    """Copyright, 2012, Alex Beal"""
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


def f(n, curr=0, nx=1):
    if n == 0:
        yield curr
    else:
        yield f(n - 1, nx, curr + nx)


def s(n, acc=0):
    if n == 0:
        yield acc
    else:
        yield s(n -1, acc + n)


print(tramp(f, 1))
print(tramp(s, 100))
