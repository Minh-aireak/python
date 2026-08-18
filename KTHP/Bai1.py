import csv

def doc_file(ten_file):
    try:
        ds = []
        with open(ten_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                so_luong = int(row['so_luong'])
                don_gia = float(row['don_gia'])
                giam_gia = int(row['giam_gia'])
                thanh_tien = tinh_thanh_tien(so_luong, don_gia, giam_gia)

                ds.append({
                    'ma_sp': row['ma_sp'],
                    'ten_sp': row['ten_sp'],
                    'so_luong': so_luong,
                    'don_gia': don_gia,
                    'giam_gia': giam_gia,
                    'thanh_tien': thanh_tien,
                    'xep_loai': xep_loai(thanh_tien)
                })

        return ds
    except FileNotFoundError:
        print("File not found!")

def tinh_thanh_tien(so_luong, don_gia, giam_gia):
    return so_luong * don_gia * (1 - giam_gia/100)

def xep_loai(thanh_tien):
    if thanh_tien >= 3000000:
        return "Bán chạy"
    elif thanh_tien < 1000000:
        return "Bán chậm"
    else:
        return "Trung bình"

def tao_noi_dung(ds):
    lines = ""
    lines += f"{'Mã sản phẩm':<15}|{'Tên sản phẩm':<15}|{'Số lượng':<15}|{'Đơn giá':<15}|{'Giảm giá':<15}|{'Thành tiền':<15}|{'Xếp loại':<15}\n"
    lines += "-" * 115 + "\n"
    for dh in ds:
        lines += f"{dh['ma_sp']:<15}|{dh['ten_sp']:<15}|{dh['so_luong']:<15}|{dh['don_gia']:<15}|{dh['giam_gia']:<15}|{dh['thanh_tien']:<15}|{dh['xep_loai']:<15}\n"
    
    lines += f"{'Thành tiền':>79}|{tinh_tong_doanh_thu(ds):>24}"

    return lines

def hien_thi(ds):
    print(tao_noi_dung(ds))

def ds_san_pham_thanh_tien_cao_nhat(ds):
    value = max(sp['thanh_tien'] for sp in ds)
    return [sp for sp in ds if sp['thanh_tien'] == value]

def thong_ke(ds):
    ban_chay = []
    trung_binh = []
    ban_cham = []

    for sp in ds:
        if sp['xep_loai'] == "Bán chạy":
            ban_chay.append(sp)
        elif sp['xep_loai'] == "Trung bình":
            trung_binh.append(sp)
        else:
            ban_cham.append(sp)
    
    return ban_chay, trung_binh, ban_cham

def tinh_tong_doanh_thu(ds):
    return sum([sp['thanh_tien'] for sp in ds])
    
def ghi_ra_txt(ten_file, ds):
    with open(ten_file, "w", encoding="utf-8-sig") as f:
        f.write(tao_noi_dung(ds))

def ghi_ra_csv(ten_file, ds):
    if not ds:
        return
    with open(ten_file, "w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ['ma_sp', 'ten_sp', 'so_luong', 'don_gia', 'giam_gia', 'thanh_tien', 'xep_loai']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ds)

if __name__ == "__main__":
    ds = doc_file("sanpham.csv")
    hien_thi(ds)

    hien_thi(ds_san_pham_thanh_tien_cao_nhat(ds))

    ban_chay, trung_binh, ban_cham = thong_ke(ds)
    print("1: Thống kế theo xếp loại 'Bán chạy'")
    hien_thi(ban_chay)
    print("2: Thống kế theo xếp loại 'Trung bình'")
    hien_thi(trung_binh)
    print("3: Thống kế theo xếp loại 'Bán chậm'")
    hien_thi(ban_cham)

    ghi_ra_txt("ketqua.txt", ds)

    ghi_ra_csv("ketqua.csv", ds)



