import math

def suma(a, b):
    c = [0,0]
    c[0] = a[0] + b[0]
    c[1] = a[1] + b[1]
    return complejoAStr(c)

def producto(a, b):
    c = [0, 0]
    c[0] = a[0] * b[0] - a[1] * b[1]
    c[1] = a[0] * b[1] + b[0] * a[1]
    return complejoAStr(c)

def resta(a, b):
    c = [0, 0]
    c[0] = a[0] - b[0]
    c[1] = a[1] - b[1]
    return complejoAStr(c)


def division(a, b):
    c = [0,0]
    x = b[0]**2 + b[1]**2
    c[0] = ((a[0] * b[0] + a[1] * b[1]) / x)
    c[1] = ((b[0] * a[1] - a[0] * b[1]) / x)
    return complejoAStr(c)

def modulo(c):
    return (c[0]**2 + c[1]**2) ** (1/2)

def conjugado(c):
    a = [0,0]
    a[0] = c[0]
    a[1] = -c[1]
    return complejoAStr(a)

def cartesianoAPolares(c):
    return ((c[0]**2 + c[1]**2)**(1/2), fase(c))

def polarACartesiano(c):
    a = [0,0]
    a[0] = math.cos(c[1]) * c[0]
    a[1] = math.sin(c[1]) * c[0]
    return complejoAStr(a)

def fase(c):
    return math.atan2(c[1], c[0])

def complejoAStr(c):
    x = " + "
    if c[1] < 0:
        x = " - "
        c[1] = -c[1]
    return str( c[0]) + x + str(c[1]) + "i"









