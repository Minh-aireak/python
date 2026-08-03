def vecinput():
    n = int(input("Nhập số phần tử của mảng: "))
    arr = []
    for i in range(n):
        val = float(input(f"Nhập phần tử thứ {i + 1}: "))
        arr.append(val)
    return arr

def vecsum(arr):
    return sum(arr)

def vecinsert(arr, index, value):
    if index < 0 or index > len(arr):
        print("Vị trí chèn không hợp lệ!")
        return arr
    arr.insert(index, value)
    return arr

def vecdel(arr, value):
    arr = [x for x in arr if x != value]
    return arr

def vecdel2(arr):
    kq = []
    for x in arr:
        if x not in kq:
            kq.append(x)
    return kq

def vecadd(arr1, arr2):
    if len(arr1) != len(arr2):
        return []
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result