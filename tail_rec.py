import types
import dis


def tramp(gen, *args, **kwargs):
    """Copyright, 2012, Alex Beal"""
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        print('+++ before: ', g)
        g = next(g)
        print('--- After  : ', g)
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
        yield s(n - 1, acc + n)


print(tramp(f, 2))
print(tramp(s, 2))

#foo.py
#+++ before : <generator object f at 0x03A09120>
#--- after  : <generator object f at 0x03A5F660>
#+++ before : <generator object f at 0x03A5F660>
#--- after  : <generator object f at 0x03A09120>
#+++ before : <generator object f at 0x03A09120>
#--- after  : 1
#1
#+++ before : <generator object s at 0x03A09120>
#--- after  : <generator object s at 0x03A5F660>
#+++ before : <generator object s at 0x03A5F660>
#--- after  : <generator object s at 0x03A09120>
#+++ before : <generator object s at 0x03A09120>
#--- after  : 3
#3

Process finished with exit code 0
