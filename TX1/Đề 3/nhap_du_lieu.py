def nhap_so(tieu_de):
    """Nhập số nguyên >= 0"""
    while True:
        ip = input(f"{tieu_de}: ").strip()
        try:
            value = int(ip)
        except ValueError:
            print(f"{tieu_de} phải là số nguyên. Nhập lại!")
            continue

        if value < 0:
            print(f"{tieu_de} không được âm. Nhập lại!")
            continue

        return value


def nhap_phieu():
    """Nhập 1 phiếu: mã NCC, ngày nhập, chi tiết (nhấn Enter trống để dừng)"""
    ma_ncc = input("Mã NCC: ").strip()
    ngay_nhap = input("Ngày nhập: ").strip()
    chi_tiet = []

    print('Nhập chi tiết (nhấn Enter trống tại "Mã hàng" để dừng):')
    while True:
        ma_hang = input("  Mã hàng: ").strip()
        if ma_hang == "":
            break

        ten_hang = input("  Tên hàng: ").strip()
        so_luong = nhap_so("  Số lượng")
        don_gia = nhap_so("  Đơn giá")

        chi_tiet.append({
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "so_luong": so_luong,
            "don_gia": don_gia
        })

    return {
        "ma_ncc": ma_ncc,
        "ngay_nhap": ngay_nhap,
        "chi_tiet": chi_tiet
    }


def nhap_phieu_nhap():
    """Yêu cầu 1: Nhập từ bàn phím từ điển phieu_nhap gồm n phiếu"""
    phieu_nhap = {}
    n = nhap_so("Số phiếu n")

    for i in range(n):
        print(f"\n--- Nhập phiếu thứ {i + 1} ---")
        while True:
            ma_phieu = input("Mã phiếu: ").strip()
            if ma_phieu == "":
                print("Mã phiếu không được trống. Nhập lại!")
                continue
            if ma_phieu in phieu_nhap:
                print(f"Mã phiếu {ma_phieu} đã tồn tại. Nhập lại!")
                continue
            break

        phieu_nhap[ma_phieu] = nhap_phieu()

    return phieu_nhap


def khoi_tao_ncc():
    """Yêu cầu 2: Khởi tạo sẵn từ điển ncc_dict (mã NCC - tên NCC)"""
    ncc_dict = {
        "NCC01": "Công ty TNHH Sách Giáo Dục",
        "NCC02": "Công ty Cổ phần Văn Phòng Phẩm",
        "NCC03": "Công ty TNHH Thiết Bị Số",
        "NCC04": "Công ty TNHH Điện Tử Việt",
        "NCC05": "Công ty Cổ phần Nhựa Minh Phát"
    }
    return ncc_dict


def nhap_bo_sung_ph001(phieu_nhap):
    """Yêu cầu 3: Nhập bổ sung phiếu PH001 nếu chưa có"""
    if "PH001" not in phieu_nhap:
        print("\nChưa có PH001 -> nhập bổ sung:")
        phieu_nhap["PH001"] = nhap_phieu()
    return phieu_nhap


def cap_nhat_phieu(phieu_nhap, ma_phieu):
    """Yêu cầu 5 (CRUD): Sửa số lượng 1 mặt hàng hoặc xóa hẳn 1 phiếu theo mã"""
    if ma_phieu not in phieu_nhap:
        print(f"Không tìm thấy phiếu {ma_phieu}!")
        return phieu_nhap

    print(f"Phiếu {ma_phieu} tồn tại. Chọn thao tác:")
    print("  1. Sửa số lượng của 1 mặt hàng")
    print("  2. Xóa hẳn phiếu")
    chon = input("Chọn: ").strip()

    if chon == "1":
        phieu = phieu_nhap[ma_phieu]
        ma_hang = input("Mã mặt hàng cần sửa: ").strip()

        for mh in phieu["chi_tiet"]:
            if mh["ma_hang"] == ma_hang:
                mh["so_luong"] = nhap_so("Số lượng mới")
                print(f"Đã sửa số lượng mặt hàng {ma_hang}!")
                return phieu_nhap

        print(f"Không tìm thấy mặt hàng {ma_hang}!")

    elif chon == "2":
        del phieu_nhap[ma_phieu]
        print(f"Đã xóa phiếu {ma_phieu}!")

    else:
        print("Chọn đúng thao tác!")

    return phieu_nhap