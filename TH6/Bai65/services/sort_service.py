# ==========================================
# SẮP XẾP THEO TÊN (A -> Z)
# ==========================================

def sort_by_name(receipt):

    receipt.products.sort(
        key=lambda product: product.name.lower()
    )

    print("Đã sắp xếp theo tên.")


# ==========================================
# SẮP XẾP THEO SỐ LƯỢNG (TĂNG)
# ==========================================

def sort_by_quantity(receipt):

    receipt.products.sort(
        key=lambda product: product.quantity
    )

    print("Đã sắp xếp theo số lượng tăng.")


# ==========================================
# SẮP XẾP THEO SỐ LƯỢNG (GIẢM)
# ==========================================

def sort_by_quantity_desc(receipt):

    receipt.products.sort(
        key=lambda product: product.quantity,
        reverse=True
    )

    print("Đã sắp xếp theo số lượng giảm.")


# ==========================================
# SẮP XẾP THEO THÀNH TIỀN (TĂNG)
# ==========================================

def sort_by_total(receipt):

    receipt.products.sort(
        key=lambda product: product.total
    )

    print("Đã sắp xếp theo thành tiền tăng.")


# ==========================================
# SẮP XẾP THEO THÀNH TIỀN (GIẢM)
# ==========================================

def sort_by_total_desc(receipt):

    receipt.products.sort(
        key=lambda product: product.total,
        reverse=True
    )

    print("Đã sắp xếp theo thành tiền giảm.")

# ==========================================
# SẮP XẾP 2 THUỘC TÍNH
#
# 1. Số lượng tăng
# 2. Nếu bằng thì thành tiền giảm
# ==========================================

def sort_by_quantity_and_total(receipt):

    receipt.products.sort(

        key=lambda product: (
            product.quantity,
            -product.total
        )

    )

    print("Đã sắp xếp theo 2 thuộc tính.")

# ==========================================
# Đơn giá giảm
# Nếu bằng -> tên tăng
# ==========================================

def sort_by_price_and_name(receipt):

    receipt.products.sort(

        key=lambda product: (
            -product.price,
            product.name.lower()
        )

    )

    print("Đã sắp xếp theo đơn giá và tên.")