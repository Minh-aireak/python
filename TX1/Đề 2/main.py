from doc_xuat_du_lieu import hien_thi, in_file
from nhap_du_lieu import doc_file, tinh_luong, nhap_cong_nhan
from xu_ly_du_lieu import (thu_nhap_cao_nhat, cn_khong_thu_nhap_0_va_tren_15trieu,
                           loc_phu_cap_tren_1trieu, xoa_cong_nhan, dem_so_ngay_cong,
                           sap_xep_thu_nhap_giam_dan, cap_nhat_phu_cap, chuyen_dict_sang_2_list)

def main():
    df = None
    while True:
        print("""
==================== MENU ====================
1. Đọc dữ liệu từ file (danh_sach_cong_nhan.csv)
2. Nhập thêm công nhân
3. Hiển thị toàn bộ danh sách (kèm luong_co_ban, tong_thu_nhap)
4. Công nhân có tổng thu nhập lớn nhất
5. Công nhân không có khoản thu nhập = 0 và tong_thu_nhap > 15,000,000
6. Lọc công nhân có phu_cap > 1,000,000
7. Xóa công nhân theo mã
8. Đếm công nhân có so_ngay_cong >= 24
9. Sắp xếp theo tong_thu_nhap giảm dần
10. Cập nhật phụ cấp CN01 thành 1,200,000
11. Ghi ra file ket_qua.csv
12. Chuyển từ điển sản phẩm sang 2 list (mã SP + số lượng)
0. Thoát!
""")

        chon = input("Chọn chức năng: ").strip()

        if chon == '1':
            df = doc_file("danh_sach_cong_nhan.csv")
            df = tinh_luong(df)
            hien_thi(df, "TOÀN BỘ DANH SÁCH CÔNG NHÂN")

        elif chon == '2':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            df = nhap_cong_nhan(df)
            hien_thi(df, "DANH SÁCH SAU KHI THÊM CÔNG NHÂN")

        elif chon == '3':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            hien_thi(df, "TOÀN BỘ DANH SÁCH CÔNG NHÂN")

        elif chon == '4':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            ds_max = thu_nhap_cao_nhat(df)
            hien_thi(ds_max, f"CÔNG NHÂN CÓ TỔNG THU NHẬP LỚN NHẤT ({ds_max['tong_thu_nhap'].iloc[0]})")

        elif chon == '5':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            ds_dieu_kien = cn_khong_thu_nhap_0_va_tren_15trieu(df)
            hien_thi(ds_dieu_kien,
                     f"CÔNG NHÂN KHÔNG CÓ KHOẢN THU NHẬP = 0 VÀ TỔNG THU NHẬP > 15,000,000 (SỐ LƯỢNG: {len(ds_dieu_kien)})")

        elif chon == '6':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            hien_thi(loc_phu_cap_tren_1trieu(df), "CÔNG NHÂN CÓ PHỤ CẤP > 1,000,000")

        elif chon == '7':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            ma = input("Nhập mã công nhân cần xóa: ").strip()
            truoc = len(df)
            df = xoa_cong_nhan(df, ma)
            sau = len(df)
            if sau < truoc:
                print(f"-> Đã xóa công nhân mã {ma}!")
            else:
                print(f"-> Không tìm thấy công nhân mã {ma}!")
            hien_thi(df, "DANH SÁCH SAU KHI XÓA")

        elif chon == '8':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            so_cn = dem_so_ngay_cong(df, 24)
            print(f"Số công nhân có số ngày công >= 24: {so_cn}")

        elif chon == '9':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            df = sap_xep_thu_nhap_giam_dan(df)
            hien_thi(df, "SAU KHI SẮP XẾP THEO TỔNG THU NHẬP GIẢM DẦN")

        elif chon == '10':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            df = cap_nhat_phu_cap(df, "CN01", 1200000)
            hien_thi(df, "SAU KHI CẬP NHẬT PHỤ CẤP CN01 = 1,200,000")

        elif chon == '11':
            if df is None:
                print("Hãy đọc dữ liệu trước (chọn 1)!")
                continue
            in_file(df, "ket_qua.csv")

        elif chon == '12':
            dict_san_pham = {
                "SP001": 10,
                "SP002": 25,
                "SP003": 15,
                "SP004": 40
            }
            print("Từ điển sản phẩm:")
            print(dict_san_pham)
            print()

            list_ma, list_so_luong = chuyen_dict_sang_2_list(dict_san_pham)
            print(f"Danh sách 1 (mã sản phẩm): {list_ma}")
            print(f"Danh sách 2 (số lượng):   {list_so_luong}")

        elif chon == '0':
            break

        else:
            print("Chọn đúng chức năng!")

if __name__ == "__main__":
    main()