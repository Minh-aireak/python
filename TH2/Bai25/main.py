from io_vector.display import input_vector, show_vector
from math_vector.operations import *

print("Nhập vector A")
A = input_vector()

print("Nhập vector B")
B = input_vector()

show_vector("A", A)
show_vector("B", B)

show_vector("A+B =", add(A, B))
show_vector("A-B =", subtract(A, B))

print("Độ dài OA =", distance(A))
print("Độ dài OB =", distance(B))

show_vector("Đối xứng A =", opposite(A))
show_vector("Đối xứng B =", opposite(B))