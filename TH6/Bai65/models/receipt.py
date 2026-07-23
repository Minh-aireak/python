class Receipt:

    def __init__(self):
        self.receipt_id = ""
        self.date = ""
        self.supplier = None
        self.product = []

    @property
    def total_money(self):
        return sum(p.total for p in self.products)

    def __str__(self):

        result = ""
        result += "=" * 75 + "\n"
        result += "{:^75}\n".format("PHIẾU NHẬP HÀNG")
        result += "=" * 75 + "\n"

        result += f"Mã phiếu : {self.receipt_id:<20}"
        result += f"Ngày lập : {self.date}\n"

        result += f"Mã NCC   : {self.supplier.supplier_id:<20}"
        result += f"Tên NCC : {self.supplier.name}\n"

        result += f"Địa chỉ  : {self.supplier.address}\n"

        result += "-" * 75 + "\n"

        result += "{:<20}{:>12}{:>12}{:>15}\n".format(
            "Tên hàng",
            "Đơn giá",
            "Số lượng",
            "Thành tiền"
        )

        result += "-" * 75 + "\n"

        for p in self.products:

            result += "{:<20}{:>12.2f}{:>12}{:>15.2f}\n".format(
                p.name,
                p.price,
                p.quantity,
                p.total
            )

        result += "-" * 75 + "\n"

        result += "{:<44}{:>31.2f}\n".format(
            "Cộng thành tiền",
            self.total_money
        )

        result += "=" * 75

        return resul