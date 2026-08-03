import pandas as pd

def doc_file(ten_file):
    return pd.read_csv(ten_file)

def tinh_luong(df):
    df["luong_co_ban"] = df["luong_ngay"] * df["so_ngay_cong"]
    df["tong_thu_nhap"] = df["luong_co_ban"] + df["phu_cap"]
    return df

def nhap_ma(df):
    """Nhập mã công nhân, kiểm tra không trống và không trùng"""
    ma_da_co = set(df["ma"]) if not df.empty else set()

    while True:
        ma = input("Mã công nhân: ").strip()
        if ma == "":
            print("Mã công nhân không được trống. Nhập lại!")
            continue
        if ma in ma_da_co:
            print(f"Mã {ma} đã tồn tại. Nhập lại!")
            continue

        return ma

def nhap_so(tieu_de):
    """Nhập số nguyên >= 0 (lương ngày, số ngày công, phụ cấp)"""
    while True:
        ip = input(f"{tieu_de}: ").strip()
        try:
            value = int(ip)
        except ValueError:
            print(f"{tieu_de} phải là số nguyên. Nhập lại!")
            continue

        if value < 0:
            print(f"{tieu_de} không được âm. Nhập lại!")
            continue

        return value

def nhap_cong_nhan(df):
    if df.empty:
        df = pd.DataFrame(columns=["ma", "ho_ten", "luong_ngay", "so-ngay_cong", "phu_cap", "luong_co_ban", "tong_thu_nhap"])

    ma = nhap_ma(df)
    ho_ten = input("Họ tên: ").strip()
    luong_ngay = nhap_so("Lương ngày")
    so_ngay_cong = nhap_so("Số ngày công")
    phu_cap = nhap_so("Phụ cấp")

    luong_co_ban = luong_ngay * so_ngay_cong
    tong_thu_nhap = luong_co_ban + phu_cap

    cong_nhan_moi = pd.DataFrame([{
        "ma": ma, "ho_ten": ho_ten, "luong_ngay": luong_ngay,
        "so_ngay_cong": so_ngay_cong, "phu_cap": phu_cap,
        "luong_co_ban": luong_co_ban, "tong_thu_nhap": tong_thu_nhap
    }])

    df = pd.concat([df, cong_nhan_moi], ignore_index=True)
    print(f"-> Đã thêm công nhân {ma} - {ho_ten} thành công!")
    return df