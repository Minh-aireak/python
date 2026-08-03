from nhap_du_lieu import tinh_dtk

def sap_xep(ds):
    return sorted(ds, key = lambda sv: -sv['diem_tong_ket'])

def list_comprehen(ds):
    return [sv for sv in ds if sv['diem_tong_ket'] >= 5.5]

def dict_comprehen(ds):
    return [{sv['ma_sv']: sv['diem_tong_ket']} for sv in ds]

def sv_dtk_cao_nhat(ds):
    dtk_max = max(sv['diem_tong_ket'] for sv in ds)
    return [sv for sv in ds if sv['diem_tong_ket'] == dtk_max]

def thong_ke(ds, xl):
    return [sv for sv in ds if sv['xep_loai'] == xl]

def xoa_theo_ten_va_diem_tong_ket(ds, ten, dtk):
    while i < len(ds):
        sv = ds[i]
        if ten.lower() in sv['ho_ten'].lower() and dtk == sv['diem_tong_ket']:
            ds.pop(i)

    print(f"Đã xóa thành công các sinh viên có tên {ten} và có điểm tổng kết {dtk}")                                      

def cap_nhat_sinh_vien(ds, msv, dcc):
    for sv in ds:
        if sv['ma_sv'].lower() == msv.lower():
            sv['diem_chuyen_can'] = dcc
            sv['diem_tong_ket'] = tinh_dtk(dcc, sv['diem_kiem_tra'], sv['diem_thi'])
            return True
    return False