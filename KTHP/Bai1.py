import csv

def doc_file(ten_file):
    ds = []
    try:
        with open(ten_file, "r", encoding = "utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader: 
                lcb = float(row['luong_co_ban'])
                snc = int(row['so_ngay_cong'])
                pc = float(row['phu_cap'])
                ltt = tinh_luong_thuc_te(lcb, snc, pc)

                ds.append({
                    'ma_nv': row['ma_nv'],
                    'ten_nv': row['ten_nv'],
                    'luong_co_ban': lcb,
                    'so_ngay_cong': snc,
                    'phu_cap': pc,
                    'luong_thuc_te': ltt,
                    'xep_loai': xep_loai(ltt)
                })
            return ds
    except FileNotFoundError:
        print("xxx File không tồn tại! xxx")

def tinh_luong_thuc_te(lcb, snc, pc):
    return (lcb / 26) * snc + pc

def xep_loai(ltt):
    if ltt >= 15000000:
        return "Xuất xắc"
    elif ltt < 7000000:
        return "Cần hỗ trợ"
    else:
        return "Đạt"

def tao_noi_dung(ds):
    lines = ""
    lines += f"{'Mã nhân viên':<15}|{'Tên nhân viên':<15}|{'Lương cơ bản':<15}|{'Số ngày công':<15}|{'Phụ cấp':<15}|{'Lương thực tế':<15}|{'Xếp loại':<15}\n"
    lines += ("-" * 115) + "\n"
    
    for nv in ds:
        lines += f"{nv['ma_nv']:<15}|{nv['ten_nv']:<15}|{nv['luong_co_ban']:<15}|{nv['so_ngay_cong']:<15}|{nv['phu_cap']:<15}|{nv['luong_thuc_te']:<15,.1f}|{nv['xep_loai']:<15}\n"

    lines += f"{'Tổng lương':<87}|{tong_quy_luong(ds):<20}"

    return lines

def hien_thi(ds):
    print(tao_noi_dung(ds))

def ds_ltt_cao_nhat(ds):
    ltt_max = max(nv['luong_thuc_te'] for nv in ds)
    return [nv for nv in ds if nv['luong_thuc_te'] == ltt_max]

def tong_quy_luong(ds):
    return sum(nv['luong_thuc_te'] for nv in ds)

def xap_xep_theo_ten_luong_co_ban(ds):
    ds = sorted(ds, key=lambda x: x['ten_nv'], reverse=True)
    ds = sorted(ds, key=lambda x: x['luong_co_ban'])
    return ds
    
def xoa_nv_co_ten(ds, ten):
    return [nv for nv in ds if ten not in nv['ten_nv']]

def cap_nhat_luong_theo_ten(ds, luong, ten):
    for nv in ds:
        if nv['ten_nv'] == ten:
            nv['luong_co_ban'] = luong

def ghi_ra_txt(ds, path):
    with open(path, "w", encoding = "utf-8-sig") as f:
        f.write(tao_noi_dung(ds))

def ghi_ra_csv(ds, path):
    with open(path, "w", encoding = "utf-8-sig", newline = "") as f:
        cot = ["ma_nv", "ten_nv", "luong_co_ban", "so_ngay_cong", "phu_cap", "luong_thuc_te", "xep_loai"]
        writer = csv.DictWriter(f, cot)
        writer.writeheader()
        writer.writerows(ds)
