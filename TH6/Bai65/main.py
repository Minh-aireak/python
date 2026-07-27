from services.input_service import *
from services.file_service import *

from services.crud_service import *

from services.sort_service import *

from services.statistic_service import *


def menu():

    print("\n=========== MENU ===========")

    print("1. Nhập phiếu")

    print("2. Đọc từ file")

    print("3. Hiển thị")

    print("4. Thêm mặt hàng")

    print("5. Xóa mặt hàng")

    print("6. Sửa mặt hàng")

    print("7. Tìm kiếm")

    print("8. Sắp xếp")

    print("9. Thống kê")

    print("10. Ghi ra file")

    print("0. Thoát")


def sort_menu():

    print("\n------ SẮP XẾP ------")

    print("1. Theo tên")

    print("2. Theo số lượng tăng")

    print("3. Theo số lượng giảm")

    print("4. Theo thành tiền tăng")

    print("5. Theo thành tiền giảm")

    print("6. Theo số lượng tăng, thành tiền giảm")

    print("7. Theo đơn giá giảm, tên tăng")


def statistic_menu():

    print("\n------ THỐNG KÊ ------")

    print("1. Tổng tiền")

    print("2. Đơn giá lớn nhất")

    print("3. Đơn giá nhỏ nhất")

    print("4. Số lượng lớn nhất")

    print("5. Số lượng nhỏ nhất")

    print("6. Thành tiền lớn nhất")

    print("7. Thành tiền nhỏ nhất")

    print("8. Đơn giá trung bình")

    print("9. Số lượng trung bình")

    print("10. Thành tiền trung bình")


def main():

    receipt = None

    while True:

        menu()

        choice = int(input("Chọn: "))

        if choice == 1:

            receipt = input_receipt()

        elif choice == 2:

            receipt = read_receipt("data/input.txt")

            print("Đọc file thành công!")

        elif choice == 3:

            if receipt is None:

                print("Chưa có dữ liệu.")

            else:

                print(receipt)

        elif choice == 4:

            add_product(receipt)

        elif choice == 5:

            delete_product(receipt)

        elif choice == 6:

            update_product(receipt)

        elif choice == 7:

            find_product(receipt)

        elif choice == 8:

            sort_menu()

            c = int(input("Chọn: "))

            if c == 1:

                sort_by_name(receipt)

            elif c == 2:

                sort_by_quantity(receipt)

            elif c == 3:

                sort_by_quantity_desc(receipt)

            elif c == 4:

                sort_by_total(receipt)

            elif c == 5:

                sort_by_total_desc(receipt)

            elif c == 6:

                sort_by_quantity_and_total(receipt)

            elif c == 7:

                sort_by_price_and_name(receipt)

        elif choice == 9:

            statistic_menu()

            c = int(input("Chọn: "))

            if c == 1:

                print("Tổng tiền:", total_money(receipt))

            elif c == 2:

                print(max_price(receipt))

            elif c == 3:

                print(min_price(receipt))

            elif c == 4:

                print(max_quantity(receipt))

            elif c == 5:

                print(min_quantity(receipt))

            elif c == 6:

                print(max_total(receipt))

            elif c == 7:

                print(min_total(receipt))

            elif c == 8:

                print(average_price(receipt))

            elif c == 9:

                print(average_quantity(receipt))

            elif c == 10:

                print(average_total(receipt))

        elif choice == 10:

            write_receipt(receipt, "data/output.txt")

            print("Đã ghi file.")

        elif choice == 0:

            print("Kết thúc chương trình.")

            break

        else:

            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
