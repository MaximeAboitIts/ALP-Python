def b(a):
    print('b(', a, ')')
    return a+a

def z(a):
    print('z(', a, ')')
    return a - 10

def a(c,d):
    print('a(', c, ',', d, ')')
    x = 0
    if c < d:
        x = b(c)
    elif c > d:
        x = b(d)
    else:
        x = z(c)
    print(x)
    return x

x = 10
x += a(x, 6)
y = a(x, x)
print('x', x)
print('y', y)