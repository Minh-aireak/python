import pickle


def in_phieu_nhap(ma_phieu, phieu, ncc_dict=None):
    """In 1 phiếu đúng dạng mẫu PHIẾU NHẬP HÀNG"""
    ten_ncc = ncc_dict.get(phieu["ma_ncc"], phieu["ma_ncc"]) if ncc_dict else phieu["ma_ncc"]

    print("=" * 60)
    print("                 PHIẾU NHẬP HÀNG")
    print("=" * 60)
    print(f"Mã phiếu : {ma_phieu}")
    print(f"Mã NCC   : {phieu['ma_ncc']}")
    print(f"Tên NCC  : {ten_ncc}")
    print(f"Ngày nhập: {phieu['ngay_nhap']}")
    print("-" * 60)
    print(f"{'Mã hàng':<10}{'Tên hàng':<20}{'Số lượng':>10}{'Đơn giá':>12}{'Thành tiền':>15}")
    print("-" * 60)

    for mh in phieu["chi_tiet"]:
        thanh_tien = mh["so_luong"] * mh["don_gia"]
        print(f"{mh['ma_hang']:<10}{mh['ten_hang']:<20}{mh['so_luong']:>10}{mh['don_gia']:>12,}{thanh_tien:>15,}")

    tong = sum(mh["so_luong"] * mh["don_gia"] for mh in phieu["chi_tiet"])
    print("-" * 60)
    print(f"{'TỔNG THÀNH TIỀN':<50}{tong:>10,}")
    print("=" * 60)
    print()


def in_phieu_nhap_dep(ma_phieu, phieu, ncc_dict=None):
    """Tạo chuỗi bản đẹp 1 phiếu đúng dạng mẫu PHIẾU NHẬP HÀNG (để ghi file)"""
    ten_ncc = ncc_dict.get(phieu["ma_ncc"], phieu["ma_ncc"]) if ncc_dict else phieu["ma_ncc"]

    lines = []
    lines.append("=" * 60)
    lines.append("                 PHIẾU NHẬP HÀNG")
    lines.append("=" * 60)
    lines.append(f"Mã phiếu : {ma_phieu}")
    lines.append(f"Mã NCC   : {phieu['ma_ncc']}")
    lines.append(f"Tên NCC  : {ten_ncc}")
    lines.append(f"Ngày nhập: {phieu['ngay_nhap']}")
    lines.append("-" * 60)
    lines.append(f"{'Mã hàng':<10}{'Tên hàng':<20}{'Số lượng':>10}{'Đơn giá':>12}{'Thành tiền':>15}")
    lines.append("-" * 60)

    for mh in phieu["chi_tiet"]:
        thanh_tien = mh["so_luong"] * mh["don_gia"]
        lines.append(f"{mh['ma_hang']:<10}{mh['ten_hang']:<20}{mh['so_luong']:>10}{mh['don_gia']:>12,}{thanh_tien:>15,}")

    tong = sum(mh["so_luong"] * mh["don_gia"] for mh in phieu["chi_tiet"])
    lines.append("-" * 60)
    lines.append(f"{'TỔNG THÀNH TIỀN':<50}{tong:>10,}")
    lines.append("=" * 60)
    lines.append("")

    return "\n".join(lines)


def ghi_file_dat(phieu_nhap, ten_file):
    """Yêu cầu 8a: Ghi toàn bộ phieu_nhap ra file .dat (đọc lại được bằng pickle)"""
    with open(ten_file, "wb") as f:
        pickle.dump(phieu_nhap, f)
    print(f"Đã ghi file {ten_file} thành công!")


def ghi_file_dep(phieu_nhap, ten_file, ncc_dict=None):
    """Yêu cầu 8b: Ghi bản đẹp đúng mẫu ra file .txt"""
    with open(ten_file, "w", encoding="utf-8") as f:
        for ma_phieu, phieu in phieu_nhap.items():
            f.write(in_phieu_nhap_dep(ma_phieu, phieu, ncc_dict))
    print(f"Đã ghi file {ten_file} thành công!")


def doc_file_dat(ten_file):
    """Yêu cầu 9: Đọc lại dữ liệu từ file .dat thành dict(list)"""
    with open(ten_file, "rb") as f:
        phieu_nhap = pickle.load(f)
    return phieu_nhap