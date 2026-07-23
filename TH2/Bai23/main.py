from convert.convert import convert_money

mile = float(input("Số dặm: "))
price = float(input("Giá 1 dặm: "))

money = mile * price

print("Tiền VND:", money)

convert_money(money)