# ==========================================
# TỔNG THÀNH TIỀN
# ==========================================

def total_money(receipt):

    return sum(product.total for product in receipt.products)


# ==========================================
# ĐƠN GIÁ LỚN NHẤT
# ==========================================

def max_price(receipt):

    return max(
        receipt.products,
        key=lambda product: product.price
    )


# ==========================================
# ĐƠN GIÁ NHỎ NHẤT
# ==========================================

def min_price(receipt):

    return min(
        receipt.products,
        key=lambda product: product.price
    )


# ==========================================
# SỐ LƯỢNG LỚN NHẤT
# ==========================================

def max_quantity(receipt):

    return max(
        receipt.products,
        key=lambda product: product.quantity
    )


# ==========================================
# SỐ LƯỢNG NHỎ NHẤT
# ==========================================

def min_quantity(receipt):

    return min(
        receipt.products,
        key=lambda product: product.quantity
    )


# ==========================================
# THÀNH TIỀN LỚN NHẤT
# ==========================================

def max_total(receipt):

    return max(
        receipt.products,
        key=lambda product: product.total
    )


# ==========================================
# THÀNH TIỀN NHỎ NHẤT
# ==========================================

def min_total(receipt):

    return min(
        receipt.products,
        key=lambda product: product.total
    )


# ==========================================
# ĐƠN GIÁ TRUNG BÌNH
# ==========================================

def average_price(receipt):

    if len(receipt.products) == 0:
        return 0

    return sum(
        product.price
        for product in receipt.products
    ) / len(receipt.products)


# ==========================================
# SỐ LƯỢNG TRUNG BÌNH
# ==========================================

def average_quantity(receipt):

    if len(receipt.products) == 0:
        return 0

    return sum(
        product.quantity
        for product in receipt.products
    ) / len(receipt.products)


# ==========================================
# THÀNH TIỀN TRUNG BÌNH
# ==========================================

def average_total(receipt):

    if len(receipt.products) == 0:
        return 0

    return sum(
        product.total
        for product in receipt.products
    ) / len(receipt.products)


# ==========================================
# ĐẾM MẶT HÀNG CÓ THÀNH TIỀN > x
# ==========================================

def count_total_greater_than(receipt, value):

    count = 0

    for product in receipt.products:

        if product.total > value:
            count += 1

    return count