from doc_xuat_du_lieu import doc_file, hien_thi, in_file
from nhap_du_lieu import nhap_sinh_vien, nhap_diem
from xu_ly_du_lieu import sap_xep, list_comprehen, dict_comprehen, sv_dtk_cao_nhat, thong_ke, xoa_theo_ten_va_diem_tong_ket, cap_nhat_sinh_vien

def main():
    ds = []
    while True:
        print("""
==================== MENU ====================
1. Đọc dữ liệu từ file
2. Nhập sinh viên
3. Hiển thị danh sách
4. Xuất ra file
5. Sắp xếp theo điểm tông kết giảm dần
6. Danh sách sinh viên có điểm tổng kết >= 5.5
7. Từ điển mã sinh viên + điểm tổng kết
8. Danh sách sinh viên có điểm tổng kết cao nhất
9. Thống kê số lượng sinh viên theo từng xếp loại
10. Xóa theo tên và điểm tổng kết
11. Cập nhật điểm tổng kết theo mã sinh viên
0. Thoát!
""")

        chon = input("Chọn chức năng: ").strip()
        if chon == '1':
            ds = doc_file("data.txt")
            hien_thi(ds)
        elif chon == '2':
            nhap_sinh_vien(ds)
            hien_thi(ds)
        elif chon == '3':
            hien_thi(ds)
        elif chon == '4':
            in_file(ds, "phieu.txt")
        elif chon == '5':
            print("-> Sắp xếp danh sách giảm dần!")
            hien_thi(sap_xep(ds))
        elif chon == '6':
            print("-> Danh sách sinh viên có điểm tổng kết >= 5.5!")
            hien_thi(list_comprehen(ds))
        elif chon == '7':
            print("-> Danh sách sinh viên theo mã sv + điểm tổng kết!")
            hien_thi(dict_comprehen(ds))
        elif chon == '8':
            print("-> Danh sách sinh viên có điểm tổng kết cao nhất")
            hien_thi(sv_dtk_cao_nhat(ds))
        elif chon == '9':
            xep_loai_map = {'1': "Giỏi", '2': "Khá", '3': "Trung bình", '4': "Yếu"}
            while True:
                print("""
====== Chọn xếp loại ======
1. Giỏi
2. Khá
3. Trung bình
4. Yếu
""")
                stt = input("Chọn xếp loại: ")
                if stt in xep_loai_map:
                    hien_thi(thong_ke(ds, xep_loai_map[stt]))
                    break
                else:
                    print("Chọn đúng xếp loại!")
        elif chon == '10':
            ten = input("Nhập tên: ")
            dtk = nhap_diem("Nhập điểm tổng kết")
            xoa_theo_ten_va_diem_tong_ket(ds, ten, dtk)
            hien_thi(ds)
        elif chon == '11':
            msv = input("Nhập mã sinh viên: ")
            dcc = nhap_diem("Nhập điểm chuyên cần")
            if cap_nhat_sinh_vien(ds, msv, dcc) is True:
                print(f"Cập nhật thành công sinh viên có mã {msv}!")
                hien_thi(ds)
            else:
                print(f"Không tìm thấy sinh viên có mã sv {msv}!")
        elif chon == '0':
            break
        else:
            print("Chọn đúng chức năng!")
            continue

if __name__ == "__main__":
    main()