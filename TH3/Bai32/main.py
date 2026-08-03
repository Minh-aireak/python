def build_matrix(a, n, m):
    k = len(a)
    if n * m > k:
        return None

    matrix = []
    for i in range(n):
        matrix.append(a[i*m : i*m + m])
        
    return matrix

def print_matrix(matrix):
    if matrix is None:
        print("==> Không thể xây dựng ma trận (không đủ phần tử)!")
        return
    for row in matrix:
        print(row)

def main():
    print("=== BÀI 3.2: MATRIX FROM LIST ===")

    # Test case 1: Đủ phần tử
    print("\n--- Test case 1: Đủ phần tử ---")
    a1 = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]
    print(f"List a = {a1}")
    n, m = 3, 4
    print(f"n = {n}, m = {m}")
    mat1 = build_matrix(a1, n, m)
    print("==> Ma trận kết quả:")
    print_matrix(mat1)

    # Test case 2: Không đủ phần tử
    print("\n--- Test case 2: Không đủ phần tử ---")
    print(f"List a = {a1}")
    n, m = 3, 7
    print(f"n = {n}, m = {m}")
    mat2 = build_matrix(a1, n, m)
    print("==> Ma trận kết quả:")
    print_matrix(mat2)

    # Test case 3: Nhập từ bàn phím
    print("\n--- Test case 3: Nhập từ bàn phím ---")
    input_str = input("Nhập list a (các số cách nhau bằng khoảng trắng): ")
    a3 = list(map(int, input_str.split()))
    n = int(input("Nhập số dòng n: "))
    m = int(input("Nhập số cột m: "))
    mat3 = build_matrix(a3, n, m)
    print("==> Ma trận kết quả:")
    print_matrix(mat3)


if __name__ == "__main__":
    main()