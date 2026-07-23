import convert

mile = float(input("Nhập số dặm bay: "))
price = float(input("Nhập tiền VND cho 1 dặm: "))

total = mile * price

print("Tổng tiền VND:", total)

convert.convert_money(total)