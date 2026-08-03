def hien_thi(df, tieu_de=""):
    if tieu_de:
        print(f"=== {tieu_de} ===")
    print(df)
    print()

def in_file(df, ten_file):
    df.to_csv(ten_file, index=False, encoding="utf-8")
    print(f"Đã ghi file {ten_file} thành công!")