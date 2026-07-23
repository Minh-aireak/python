from models.product import Product
from models.supplier import Supplier
from models.receipt import Receipt


def input_supplier():

    supplier = Supplier()

    supplier.supplier_id = input("Mã NCC: ")
    supplier.name = input("Tên NCC: ")
    supplier.address = input("Địa chỉ: ")

    return supplier


def input_product():

    name = input("Tên hàng: ")
    price = float(input("Đơn giá: "))
    quantity = int(input("Số lượng: "))

    return Product(name, price, quantity)


def input_receipt():

    receipt = Receipt()

    receipt.receipt_id = input("Mã phiếu: ")
    receipt.date = input("Ngày lập: ")

    receipt.supplier = input_supplier()

    n = int(input("Số mặt hàng: "))

    for i in range(n):
        print(f"\n--- Mặt hàng {i+1} ---")
        receipt.products.append(input_product())

    return receipt