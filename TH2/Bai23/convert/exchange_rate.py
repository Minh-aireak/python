from rate import exchange_rate

def convert_money(vnd):
    print("USD:", round(vnd / exchange_rate.USD,2))
    print("EUR:", round(vnd / exchange_rate.EUR,2))
    print("JPY:", round(vnd / exchange_rate.JPY,2))