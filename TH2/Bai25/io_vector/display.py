def input_vector():
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    return (x, y, z)

def show_vector(name, v):
    print(f"{name}({v[0]}, {v[1]}, {v[2]})")