import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm kiểm tra số đối xứng
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Nhập S và E
while True:
    S = int(input("Nhập S: "))
    E = int(input("Nhập E: "))

    if S < E and E <= 99999999:
        break
    else:
        print("Nhập sai! Vui lòng nhập lại.")

tong = 0

for i in range(S, E + 1):
    if is_prime(i) and is_palindrome(i):
        tong += i

print("Tổng các số vừa nguyên tố vừa đối xứng:", tong)