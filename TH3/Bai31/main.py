from myvector import vecinput, vecsum, vecinsert, vecdel, vecadd, vecdel2

def main():
    print("=== BÀI 3.1: VECTOR LIB ===")
    print("\n1. Nhập mảng thứ nhất:")
    arr1 = vecinput()
    print(f"==> Mảng thứ nhất: {arr1}")

    print("\n2. Nhập mảng thứ hai:")
    arr2 = vecinput()
    print(f"==> Mảng thứ hai: {arr2}")

    # Tính tổng
    print("\n3. Tổng các phần tử: ")
    print(f"==> Mảng 1: {vecsum(arr1)}")
    print(f"==> Mảng 2: {vecsum(arr2)}")

    # Chèn phần tử
    val = float(input("\n4. Nhập giá trị cần chèn vào mảng 1: "))
    idx = int(input("Nhập vị trí cần chèn: "))
    arr1 = vecinsert(arr1, idx, val)
    print(f"==> Mảng 1 sau khi chèn: {arr1}")

    # Xóa phần tử 1 
    value = float(input("\n5. Nhập giá cần xóa trong mảng 1: "))
    arr1 = vecdel(arr1, value)
    print(f"==> Mảng 1 sau khi xóa: {arr1}")

    # Xóa phần tử 2
    arr1 = vecdel2(arr1)
    print(f"==> Mảng sau khi xóa các phần tử giống nhau trong mảng: {arr1}")

    # Cộng hai mảng
    print("\n6. Cộng hai mảng:")
    result = vecadd(arr1, arr2)
    if len(result) == 0:
        print("==> Hai mảng khác kích thước, không thể cộng!")
    else:
        print(f"==> Kết quả: {result}")


if __name__ == "__main__":
    main()