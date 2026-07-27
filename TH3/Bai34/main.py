"""
Bài 3.4 - Merge Sorted Lists
Trộn hai mảng số nguyên đã được sắp xếp tăng dần
"""


def input_array(label):
    """Nhập mảng số nguyên từ bàn phím"""
    print(f"Nhập mảng {label}:")
    n = int(input(f"  Số phần tử của mảng {label}: "))
    arr = []
    for i in range(n):
        val = int(input(f"  Nhập phần tử thứ {i + 1}: "))
        arr.append(val)
    return arr


def merge_sorted(a, b):
    """
    Trộn hai mảng đã được sắp xếp a và b thành mảng c cũng được sắp xếp.
    Giả sử a và b đã được sắp tăng dần.
    """
    c = []
    i, j = 0, 0
    n, m = len(a), len(b)

    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # Lấy phần còn lại từ a
    while i < n:
        c.append(a[i])
        i += 1

    # Lấy phần còn lại từ b
    while j < m:
        c.append(b[j])
        j += 1

    return c


def print_test_case(label, a, b):
    """In kết quả test case"""
    print(f"\n{label}")
    print(f"  a (đã sắp xếp) = {a}")
    print(f"  b (đã sắp xếp) = {b}")
    c = merge_sorted(a, b)
    print(f"  c = {c}")


def main():
    print("=== BÀI 3.4: MERGE SORTED LISTS ===")

    # Test case 1: n < m
    print_test_case(
        "Test case 1: n < m",
        [1, 3, 5],
        [2, 4, 6, 8, 10]
    )

    # Test case 2: n > m
    print_test_case(
        "Test case 2: n > m",
        [1, 3, 5, 7, 9, 11],
        [2, 4, 6]
    )

    # Test case 3: n = m
    print_test_case(
        "Test case 3: n = m",
        [1, 3, 5, 7],
        [2, 4, 6, 8]
    )

    # Test case 4: Có phần tử trùng nhau
    print_test_case(
        "Test case 4: Có phần tử trùng nhau",
        [1, 2, 3, 4, 5],
        [3, 4, 5, 6, 7]
    )

    # Test case 5: Một mảng rỗng
    print_test_case(
        "Test case 5: Một mảng rỗng",
        [],
        [1, 2, 3]
    )

    # Test case 6: Nhập từ bàn phím
    print("\n--- Test case 6: Nhập từ bàn phím ---")
    a = input_array("a")
    b = input_array("b")

    # Sắp xếp a và b tăng dần
    a.sort()
    b.sort()
    print(f"\na sau khi sắp xếp = {a}")
    print(f"b sau khi sắp xếp = {b}")

    c = merge_sorted(a, b)
    print(f"c = {c}")


if __name__ == "__main__":
    main()