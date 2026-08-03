def tinh_thanh_tien(phieu):
    """Tính tổng thành tiền của 1 phiếu: tổng (so_luong * don_gia) của các mặt hàng"""
    return sum(mh["so_luong"] * mh["don_gia"] for mh in phieu["chi_tiet"])


def xoa_mat_hang_so_luong_0(phieu_nhap):
    """Yêu cầu 4: Xóa các mặt hàng có số lượng = 0.
    Nếu phiếu không còn mặt hàng nào thì xóa luôn phiếu đó."""
    phieu_nhap_moi = {}
    for ma_phieu, phieu in phieu_nhap.items():
        chi_tiet_moi = [mh for mh in phieu["chi_tiet"] if mh["so_luong"] > 0]
        if chi_tiet_moi:
            phieu["chi_tiet"] = chi_tiet_moi
            phieu_nhap_moi[ma_phieu] = phieu

    return phieu_nhap_moi


def chuyen_sang_2_list(phieu_nhap):
    """Yêu cầu 6: list1 = mã phiếu, list2 = tổng thành tiền tương ứng"""
    list1 = list(phieu_nhap.keys())
    list2 = [tinh_thanh_tien(phieu) for phieu in phieu_nhap.values()]
    return list1, list2


def sap_xep_theo_tong_thanh_tien(phieu_nhap, ncc_dict):
    """Yêu cầu 7: Sắp xếp theo tổng thành tiền giảm dần,
    nếu bằng nhau thì theo mã NCC tăng dần.
    Trả về danh sách các bộ (ma_phieu, phieu, tong_thanh_tien) đã sắp xếp."""
    danh_sach = []
    for ma_phieu, phieu in phieu_nhap.items():
        danh_sach.append((ma_phieu, phieu, tinh_thanh_tien(phieu)))

    danh_sach.sort(key=lambda x: (-x[2], x[1]["ma_ncc"]))
    return danh_sach