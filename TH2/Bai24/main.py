import point

A = tuple(map(float, input("Nhập A(x y): ").split()))
B = tuple(map(float, input("Nhập B(x y): ").split()))
C = tuple(map(float, input("Nhập C(x y): ").split()))

dA = point.distance(*A)
dB = point.distance(*B)
dC = point.distance(*C)

points = {
    "A": dA,
    "B": dB,
    "C": dC
}

gan = min(points, key=points.get)
xa = max(points, key=points.get)

print("Điểm gần O nhất:", gan)
print("Điểm xa O nhất:", xa)

print("Diện tích tam giác:", point.area(A, B, C))