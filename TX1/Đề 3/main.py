from doc_xuat_du_lieu import (in_phieu_nhap, ghi_file_dat, ghi_file_dep, doc_file_dat)
from nhap_du_lieu import (nhap_phieu_nhap, khoi_tao_ncc, nhap_bo_sung_ph001,
                          cap_nhat_phieu)
from xu_ly_du_lieu import (xoa_mat_hang_so_luong_0, chuyen_sang_2_list,
                           sap_xep_theo_tong_thanh_tien, tinh_thanh_tien)


def main():
    # Yêu cầu 1: Nhập từ điển phieu_nhap
    print("===== YÊU CẦU 1: NHẬP PHIẾU NHẬP =====")
    phieu_nhap = nhap_phieu_nhap()

    # Yêu cầu 2: Khởi tạo ncc_dict
    print("\n===== YÊU CẦU 2: TỪ ĐIỂN NCC =====")
    ncc_dict = khoi_tao_ncc()
    for ma, ten in ncc_dict.items():
        print(f"{ma}: {ten}")

    # Yêu cầu 3: Kiểm tra PH001
    print("\n===== YÊU CẦU 3: KIỂM TRA PH001 =====")
    if "PH001" in phieu_nhap:
        print("Có mã phiếu PH001. In phiếu đó:")
        in_phieu_nhap("PH001", phieu_nhap["PH001"], ncc_dict)
    else:
        print("Không có mã phiếu PH001 -> nhập bổ sung.")
        phieu_nhap = nhap_bo_sung_ph001(phieu_nhap)
        print("Đã thêm PH001 vào phieu_nhap.")

    # Yêu cầu 4: Xóa mặt hàng số lượng = 0
    print("\n===== YÊU CẦU 4: XÓA MẶT HÀNG CÓ SỐ LƯỢNG = 0 =====")
    phieu_nhap = xoa_mat_hang_so_luong_0(phieu_nhap)
    print("Danh sách phiếu sau khi xóa mặt hàng số lượng = 0:")
    for ma_phieu, phieu in phieu_nhap.items():
        print(f"  {ma_phieu}: {len(phieu['chi_tiet'])} mặt hàng")

    # Yêu cầu 5: CRUD cơ bản
    print("\n===== YÊU CẦU 5: CRUD THEO MÃ PHIẾU =====")
    ma_phieu = input("Nhập mã phiếu cần sửa/xóa: ").strip()
    phieu_nhap = cap_nhat_phieu(phieu_nhap, ma_phieu)

    # Yêu cầu 6: Chuyển sang 2 list
    print("\n===== YÊU CẦU 6: CHUYỂN SANG 2 LIST =====")
    list1, list2 = chuyen_sang_2_list(phieu_nhap)
    print(f"List1 (mã phiếu): {list1}")
    print(f"List2 (tổng thành tiền): {list2}")

    n = len(list1)
    if n > 0:
        print(f"3 phần tử đầu của list1: {list1[:3]}")
        print(f"3 phần tử cuối của list2: {list2[-3:]}")

    # Yêu cầu 7: Sắp xếp theo tổng thành tiền giảm dần, mã NCC tăng dần
    print("\n===== YÊU CẦU 7: SẮP XẾP PHIẾU =====")
    danh_sach_sx = sap_xep_theo_tong_thanh_tien(phieu_nhap, ncc_dict)
    print("=" * 60)
    print("DANH SÁCH PHIẾU SẮP XẾP THEO TỔNG THÀNH TIỀN GIẢM DẦN")
    print("=" * 60)
    print(f"{'Mã phiếu':<10}{'Mã NCC':<8}{'Tên NCC':<30}{'Tổng thành tiền':>15}")
    print("-" * 60)
    for ma_p, phieu, tong in danh_sach_sx:
        ten_ncc = ncc_dict.get(phieu["ma_ncc"], phieu["ma_ncc"])
        print(f"{ma_p:<10}{phieu['ma_ncc']:<8}{ten_ncc:<30}{tong:>15,}")
    print()

    # Yêu cầu 8: Ghi file .dat và .txt
    print("\n===== YÊU CẦU 8: GHI FILE =====")
    ghi_file_dat(phieu_nhap, "phieunhap2.dat")
    ghi_file_dep(phieu_nhap, "phieunhap2_dep.txt", ncc_dict)

    # Yêu cầu 9: Đọc lại file .dat
    print("\n===== YÊU CẦU 9: ĐỌC LẠI FILE .dat =====")
    phieu_doc_lai = doc_file_dat("phieunhap2.dat")
    print("Dữ liệu đọc lại từ phieunhap2.dat:")
    for ma_phieu, phieu in phieu_doc_lai.items():
        in_phieu_nhap(ma_phieu, phieu, ncc_dict)


if __name__ == "__main__":
    main()