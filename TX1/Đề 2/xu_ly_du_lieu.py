def thu_nhap_cao_nhat(df):
    """TODO 4: Tìm tổng thu nhập lớn nhất -> lọc các dòng có tong_thu_nhap bằng giá trị đó"""
    max_thu_nhap = df["tong_thu_nhap"].max()
    return df[df["tong_thu_nhap"] == max_thu_nhap]

def cn_khong_thu_nhap_0_va_tren_15trieu(df):
    """TODO 5: Lọc công nhân không có khoản thu nhập nào = 0 và tong_thu_nhap > 15,000,000"""
    dieu_kien = (df["luong_co_ban"] != 0) & (df["phu_cap"] != 0) & (df["tong_thu_nhap"] > 15000000)
    return df[dieu_kien]

def loc_phu_cap_tren_1trieu(df):
    """TODO 6 (LỌC): Lọc ra công nhân có phu_cap > 1,000,000"""
    return df[df["phu_cap"] > 1000000]

def xoa_cong_nhan(df, ma):
    """TODO 7 (XÓA): Xóa công nhân có mã cho trước khỏi df, reset index"""
    return df[df["ma"] != ma].reset_index(drop=True)

def xoa_cong_nhan(df, ma):
    idx = df[df["ma"] == ma].index    # tìm index của dòng cần xoá
    return df.drop(idx).reset_index(drop=True)

def dem_so_ngay_cong(df, so_ngay):
    """TODO 8 (ĐẾM): Đếm số công nhân có so_ngay_cong >= số ngày cho trước"""
    return (df["so_ngay_cong"] >= so_ngay).sum()

def sap_xep_thu_nhap_giam_dan(df):
    """TODO 9 (SẮP XẾP): Sắp xếp df theo tong_thu_nhap giảm dần"""
    return df.sort_values("tong_thu_nhap", ascending=False).reset_index(drop=True)

def cap_nhat_phu_cap(df, ma, phu_cap_moi):
    """TODO 10 (SỬA): Cập nhật phu_cap của công nhân theo mã rồi tính lại tong_thu_nhap"""
    df.loc[df["ma"] == ma, "phu_cap"] = phu_cap_moi
    df.loc[df["ma"] == ma, "tong_thu_nhap"] = (
        df.loc[df["ma"] == ma, "luong_co_ban"] + df.loc[df["ma"] == ma, "phu_cap"]
    )
    return df

def chuyen_dict_sang_2_list(dict_sp):
    list_ma = list(dict_sp.keys())
    list_so_luong = list(dict_sp.values())
    return list_ma, list_so_luong
