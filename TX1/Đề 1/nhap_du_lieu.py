def tinh_dtk(dcc, dkt, dt):
    return 0.1 * dcc + 0.3 * dkt + 0.6 * dt

def tinh_xl(dtk):
    if dtk >= 8.5 and dtk <= 10:
        return "Giỏi"
    elif dtk >= 7.0 and dtk < 8.5:
        return "Khá"
    elif dtk >= 5.5 and dtk < 7:
        return "Trung bình"
    else:
        return "Yếu"

def nhap_ma_sv(ds):
    ma_sv_da_co = [sv['ma_sv'] for sv in ds]
    while True:
        ma_sv = input("Mã SV: ").strip()
        if ma_sv == "":
            print("Mã SV không trống. Nhập lại!")
            continue
        if ma_sv in ma_sv_da_co:
            print("Mã SV trùng. Nhập lại!")
            continue
        
        return ma_sv

def nhap_diem(diem):
    while True:
        ip = input(f"{diem}: ").strip()
        try:
            value = float(ip)
        except ValueError:
            print("Điểm phải là số. Nhập lại!")
            continue

        if value < 0 or value > 10:
            print("Điểm nằm trong khoảng [0, 10]. Nhập lại!")
            continue

        return value

def nhap_sinh_vien(ds):
    ma_sv = nhap_ma_sv(ds)
    ho_ten = input("Họ tên: ").strip()
    diem_chuyen_can = nhap_diem("Điểm chuyên cần")
    diem_kiem_tra = nhap_diem("Điểm kiểm tra")
    diem_thi = nhap_diem("Điểm thi")
    diem_tong_ket = tinh_dtk(diem_chuyen_can, diem_kiem_tra, diem_thi)
    xep_loai = tinh_xl(diem_tong_ket)

    return ds.append({'ma_sv': ma_sv, 'ho_ten': ho_ten, 'diem_chuyen_can': diem_chuyen_can,
     'diem_kiem_tra': diem_kiem_tra, 'diem_thi': diem_thi, 'diem_tong_ket': diem_tong_ket, 'xep_loai': xep_loai})