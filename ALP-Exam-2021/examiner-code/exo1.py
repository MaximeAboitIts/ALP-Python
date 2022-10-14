def z(z):
    print("z(z)")
    print("z", z)
    y(z*2)
    print("z",z)

def y(z):
    print("y(z)")
    print("z", z)
    z -= 1
    print("z", z)

print("=== A ===")
z(4)