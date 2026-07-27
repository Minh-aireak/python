"""
Module myvector - thao tác trên mảng một chiều sử dụng list
"""


def vecinput():
    """Nhập mảng từ bàn phím"""
    n = int(input("Nhập số phần tử của mảng: "))
    arr = []
    for i in range(n):
        val = float(input(f"Nhập phần tử thứ {i + 1}: "))
        arr.append(val)
    return arr


def vecsum(arr):
    """Tính tổng các phần tử trong mảng"""
    total = 0
    for val in arr:
        total += val
    return total


def vecinsert(arr, index, value):
    """Chèn phần tử vào mảng tại vị trí index"""
    if index < 0 or index > len(arr):
        print("Vị trí chèn không hợp lệ!")
        return arr
    arr.insert(index, value)
    return arr


def vecdel(arr, index):
    """Xóa phần tử trong mảng tại vị trí index"""
    if index < 0 or index >= len(arr):
        print("Vị trí xóa không hợp lệ!")
        return arr
    arr.pop(index)
    return arr


def vecadd(arr1, arr2):
    """Cộng hai mảng cùng kích thước. Nếu khác kích thước, trả về mảng rỗng."""
    if len(arr1) != len(arr2):
        return []
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result