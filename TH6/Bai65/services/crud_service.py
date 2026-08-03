from models.product import Product


# ==========================================
# THÊM MẶT HÀNG
# ==========================================

def add_product(receipt):

    print("\n===== THÊM MẶT HÀNG =====")

    name = input("Tên hàng: ")

    # Kiểm tra trùng tên
    for product in receipt.products:
        if product.name.lower() == name.lower():
            print("Tên hàng đã tồn tại!")
            return

    price = float(input("Đơn giá: "))
    quantity = int(input("Số lượng: "))

    receipt.products.append(
        Product(name, price, quantity)
    )

    print("Thêm thành công!")


# ==========================================
# XÓA MẶT HÀNG
# ==========================================

def delete_product(receipt):

    print("\n===== XÓA MẶT HÀNG =====")

    name = input("Tên cần xóa: ")

    for product in receipt.products:

        if product.name.lower() == name.lower():

            receipt.products.remove(product)

            print("Đã xóa.")

            return

    print("Không tìm thấy.")


# ==========================================
# SỬA MẶT HÀNG
# ==========================================

def update_product(receipt):

    print("\n===== SỬA MẶT HÀNG =====")

    name = input("Tên cần sửa: ")

    for product in receipt.products:

        if product.name.lower() == name.lower():

            print("\nNhập thông tin mới")

            product.name = input("Tên: ")

            product.price = float(input("Đơn giá: "))

            product.quantity = int(input("Số lượng: "))

            print("Cập nhật thành công.")

            return

    print("Không tìm thấy.")


# ==========================================
# TÌM KIẾM
# ==========================================

def find_product(receipt):

    print("\n===== TÌM KIẾM =====")

    keyword = input("Tên hàng: ")

    found = False

    for product in receipt.products:

        if keyword.lower() in product.name.lower():

            print(product)

            found = True

    if not found:
        print("Không có dữ liệu.")