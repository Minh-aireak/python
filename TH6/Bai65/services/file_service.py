from models.product import Product
from models.supplier import Supplier
from models.receipt import Receipt


def read_receipt(path):
    """
    Đọc phiếu nhập từ file
    """

    receipt = Receipt()

    with open(path, "r", encoding="utf-8") as file:

        receipt.receipt_id = file.readline().strip()
        receipt.date = file.readline().strip()

        supplier = Supplier(
            file.readline().strip(),
            file.readline().strip(),
            file.readline().strip()
        )

        receipt.supplier = supplier

        n = int(file.readline())

        for _ in range(n):

            line = file.readline().strip()

            if line == "":
                continue

            name, price, quantity = line.split(",")

            receipt.products.append(
                Product(
                    name,
                    float(price),
                    int(quantity)
                )
            )

    return receipt


def write_receipt(receipt, path):
    """
    Ghi phiếu nhập ra file
    """

    with open(path, "w", encoding="utf-8") as file:
        file.write(str(receipt))


def print_receipt(receipt):
    """
    In ra màn hình
    """

    print(receipt)