"""
Chương trình sử dụng module myvector
Bài 3.1 - Vector Lib
"""

from myvector import vecinput, vecsum, vecinsert, vecdel, vecadd


def main():
    print("=== BÀI 3.1: VECTOR LIB ===")
    print("\n1. Nhập mảng thứ nhất:")
    arr1 = vecinput()
    print(f"Mảng thứ nhất: {arr1}")

    print("\n2. Nhập mảng thứ hai:")
    arr2 = vecinput()
    print(f"Mảng thứ hai: {arr2}")

    # Tính tổng
    print(f"\n3. Tổng các phần tử mảng 1: {vecsum(arr1)}")
    print(f"   Tổng các phần tử mảng 2: {vecsum(arr2)}")

    # Chèn phần tử
    val = float(input("\n4. Nhập giá trị cần chèn vào mảng 1: "))
    idx = int(input("   Nhập vị trí cần chèn: "))
    arr1 = vecinsert(arr1, idx, val)
    print(f"   Mảng 1 sau khi chèn: {arr1}")

    # Xóa phần tử
    idx = int(input("\n5. Nhập vị trí cần xóa trong mảng 1: "))
    arr1 = vecdel(arr1, idx)
    print(f"   Mảng 1 sau khi xóa: {arr1}")

    # Cộng hai mảng
    print("\n6. Cộng hai mảng:")
    result = vecadd(arr1, arr2)
    if len(result) == 0:
        print("   Hai mảng khác kích thước, không thể cộng!")
    else:
        print(f"   Kết quả: {result}")


if __name__ == "__main__":
    main()