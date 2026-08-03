def is_numeric_string(s):
    if len(s) == 0:
        return False
    for ch in s:
        if ch < '0' or ch > '9':
            return False
    return True

def count_numeric_strings(t):
    count = 0
    for item in t:
        if item.isdigit():
            count += 1
    return count

def print_test_case(label, a):
    print(f"\n{label}")
    print(f"List a = {a}")
    b = (a)
    print(f"Tuple b = {b}")
    count = count_numeric_strings(b)
    print(f"Số phần tử có dạng số: {count}")

def main():
    print("=== BÀI 3.5: TUPLE FROM LIST ===")

    # Test case 1: Hỗn hợp số và chữ
    print_test_case(
        "Test case 1: Hỗn hợp số và chữ",
        ['123', 'hello', '456', 'world', '789']
    )

    # Test case 2: Toàn bộ là số
    print_test_case(
        "Test case 2: Toàn bộ là dạng số",
        ['123', '456', '789', '030', '001']
    )

    # Test case 3: Toàn bộ không phải số
    print_test_case(
        "Test case 3: Toàn bộ không phải dạng số",
        ['hello', 'world', 'python', 'a13', 'test']
    )

    # Test case 4: Có số 0 ở đầu, xâu rỗng
    print_test_case(
        "Test case 4: Có số 0 ở đầu, xâu rỗng, hỗn hợp",
        ['030', '', '123abc', '000', '12', 'abc']
    )

    # Test case 5: Nhập từ bàn phím
    print("\n--- Test case 5: Nhập từ bàn phím ---")
    input_str = input("Nhập các xâu (cách nhau bằng khoảng trắng): ")
    a5 = input_str.split()
    print_test_case("Kết quả nhập từ bàn phím", a5)

if __name__ == "__main__":
    main()