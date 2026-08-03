from nhap_du_lieu import tinh_dtk, tinh_xl

def tao_noi_dung(ds):
    lines = ""
    lines += f"{'BẢNG ĐIỂM SINH VIÊN':^105}" + "\n"
    lines += ("-" * 105) + "\n"
    lines += f"{'Mã SV':<9}{'Họ tên':>15}{'Điểm chuyên cần':>19}"
    lines += f"{'Điểm kiểm tra':>16}{'Điểm thi':>14}{'Điểm tổng kết':>16}{'Xếp loại':>15}\n"
    lines += ("-" * 105) + "\n"

    for sv in ds:
        lines += f"{sv['ma_sv']:<9}{sv['ho_ten']:>15}{sv['diem_chuyen_can']:>19,.2f}"
        lines += f"{sv['diem_kiem_tra']:>16,.2f}{sv['diem_thi']:>14,.2f}{sv['diem_tong_ket']:>16,.2f}{sv['xep_loai']:>15}\n"

    return lines

def hien_thi(ds):
    print(tao_noi_dung(ds))

def in_file(ds, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write(tao_noi_dung(ds))
    print("-> In ra file thành công!")

def doc_file(ten_file):
    ds = []
    with open(ten_file, "r", encoding="utf-8") as f:
        for line in f:
            ma_sv, ho_ten, dcc, dkt, dt = line.strip().split(",")
            diem_chuyen_can = float(dcc)
            diem_kiem_tra = float(dcc)
            diem_thi = float(dt)
            diem_tong_ket = tinh_dtk(diem_chuyen_can, diem_kiem_tra, diem_thi)
            xep_loai = tinh_xl(diem_tong_ket)
            ds.append({'ma_sv': ma_sv, 'ho_ten': ho_ten, 'diem_chuyen_can': diem_chuyen_can, 'diem_kiem_tra': diem_kiem_tra,
             'diem_thi': diem_thi, 'diem_tong_ket': diem_tong_ket, 'xep_loai': xep_loai})
    print("-> Đọc thành công file!")
    return ds