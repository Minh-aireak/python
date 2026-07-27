def merge_lists(a, b):
    result = []
    i, j = 0, 0
    n, m = len(a), len(b)

    # Xen kẽ từng phần tử
    while i < n and j < m:
        result.append(a[i])
        i += 1
        result.append(b[j])
        j += 1

    # Lấy phần còn lại từ a (nếu a còn)
    while i < n:
        result.append(a[i])
        i += 1

    # Lấy phần còn lại từ b (nếu b còn)
    while j < m:
        result.append(b[j])
        j += 1

    return result


def print_test_case(label, a, b):
    print(f"\n{label}")
    print(f"  a = {a}")
    print(f"  b = {b}")
    c = merge_lists(a, b)
    print(f"  c = {c}")


def main():
    print("=== BÀI 3.3: MERGE LISTS ===")

    # Test case 1: a dài hơn b
    print_test_case(
        "Test case 1: a dài hơn b",
        ['a', 'b', 'c', 'd', 'e'],
        [1, 2, 3]
    )

    # Test case 2: a dài bằng b
    print_test_case(
        "Test case 2: a dài bằng b",
        ['x', 'y', 'z'],
        [10, 20, 30]
    )

    # Test case 3: a ngắn hơn b
    print_test_case(
        "Test case 3: a ngắn hơn b",
        ['a', 'b', 'c'],
        [1, 2, 3, 4, 5]
    )

    # Test case 4: a và b chứa toàn số
    print_test_case(
        "Test case 4: a và b chứa toàn số",
        [1, 3, 5, 7, 9],
        [2, 4, 6]
    )

    # Test case 5: a chứa xâu, b chứa số
    print_test_case(
        "Test case 5: a chứa xâu ký tự, b chứa số",
        ['hello', 'world', 'python'],
        [100, 200, 300, 400]
    )

    # Test case 6: Nhập từ bàn phím
    print("\n--- Test case 6: Nhập từ bàn phím ---")
    a_input = input("Nhập danh sách a (các phần tử cách nhau bằng khoảng trắng): ").split()
    # Thử chuyển sang số nếu có thể
    arr_a = []
    for x in a_input:
        arr_a.append(x)

    b_input = input("Nhập danh sách b (các phần tử cách nhau bằng khoảng trắng): ").split()
    arr_b = []
    for x in b_input:
        arr_b.append(x)

    c = merge_lists(arr_a, arr_b)
    print(f"  a = {arr_a}")
    print(f"  b = {arr_b}")
    print(f"  c = {c}")


if __name__ == "__main__":
    main()