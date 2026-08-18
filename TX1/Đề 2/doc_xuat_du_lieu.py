def hien_thi(df, tieu_de=""):
    if tieu_de:
        print(f"=== {tieu_de} ===")
    print(df)
    print()

def in_file(df, ten_file):
    df.to_csv(ten_file, index=False, encoding="utf-8")
    print(f"Đã ghi file {ten_file} thành công!")



    def in_bang(ds, tieu_de="DANH SÁCH SINH VIÊN"):
    print(f"\n{tieu_de:^100}")
    print("-" * 92)
    print(f"|{'Mã SV':^10}|{'Họ tên':^25}|{'Năm sinh':^10}|{'G.Tính':^10}|{'Quê quán':^20}|{'Điểm':^10}|")
    print("-" * 92)
    for sv in ds:
        print(
            f"|{sv['Mã sinh viên']:^10}"
            f"|{sv['Họ tên']:<25}"
            f"|{sv['Năm sinh']:^10}"
            f"|{sv['Giới tính']:^10}"
            f"|{sv['Quê quán']:^20}"
            f"|{sv['Điểm thi']:^10}|"
        )
    print("-" * 92)