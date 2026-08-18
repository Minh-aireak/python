import csv
import os
from abc inport ABC, abstractmethod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DonHang:
    """Đối tượng đại diện cho một dòng dữ liệu trong file CSV."""

    def __init__(self, ma_don, ma_sp, ten_sp, don_gia, loai, ty_le_giam, ma_nv, ho_ten, so_luong, ngay_ban):
        self.ma_don = ma_don
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.don_gia = float(don_gia)
        self.loai = loai
        self.ty_le_giam = float(ty_le_giam)
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.so_luong = int(so_luong)
        self.ngay_ban = ngay_ban

    @classmethod
    def doc_tu_csv(cls, duong_dan_csv):
        danh_sach = []
        with open(duong_dan_csv, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                don_hang = cls(
                    ma_don=row["ma_don"],
                    ma_sp=row["ma_sp"],
                    ten_sp=row["ten_sp"],
                    don_gia=row["don_gia"],
                    loai=row["loai"],
                    ty_le_giam=row["ty_le_giam"],
                    ma_nv=row["ma_nv"],
                    ho_ten=row["ho_ten"],
                    so_luong=row["so_luong"],
                    ngay_ban=row["ngay_ban"],
                )
                danh_sach.append(don_hang)
        return danh_sach

    def tinh_gia_ban(self):
        """Giá bán = đơn giá * (1 - tỷ lệ giảm) nếu loại khuyến mãi, ngược lại = đơn giá."""
        if self.loai == "khuyen_mai":
            return self.don_gia * (1 - self.ty_le_giam)
        return self.don_gia

    def tinh_thanh_tien(self):
        """Thành tiền = số lượng * giá bán."""
        return self.so_luong * self.tinh_gia_ban()

    def to_dict(self):
        """Chuyển đối tượng thành dictionary để ghi ra file CSV."""
        return {
            "ma_don": self.ma_don,
            "ma_sp": self.ma_sp,
            "ten_sp": self.ten_sp,
            "don_gia": self.don_gia,
            "loai": self.loai,
            "ty_le_giam": self.ty_le_giam,
            "ma_nv": self.ma_nv,
            "ho_ten": self.ho_ten,
            "so_luong": self.so_luong,
            "ngay_ban": self.ngay_ban,
            "gia_ban": round(self.tinh_gia_ban(), 2),
            "thanh_tien": round(self.tinh_thanh_tien(), 2),
        }

    def __str__(self):
        return (f"DonHang(ma_don={self.ma_don}, ma_sp={self.ma_sp}, ten_sp={self.ten_sp}, "
                f"don_gia={self.don_gia}, loai={self.loai}, ty_le_giam={self.ty_le_giam}, "
                f"ma_nv={self.ma_nv}, ho_ten={self.ho_ten}, so_luong={self.so_luong}, "
                f"ngay_ban={self.ngay_ban})")


class QuanLyDonHang:
    """Quản lý danh sách đối tượng DonHang đọc từ file CSV."""

    def __init__(self, duong_dan_csv):
        self.duong_dan_csv = duong_dan_csv
        # Sử dụng classmethod DonHang.doc_tu_csv để đọc file
        self.danh_sach_don_hang = DonHang.doc_tu_csv(duong_dan_csv)

    @classmethod
    def tao_tu_csv(cls, duong_dan_csv):
        """
        Classmethod: Tạo đối tượng QuanLyDonHang trực tiếp từ file CSV.
        """
        return cls(duong_dan_csv)

    def ghi_csv(self, duong_dan_xuat):
        """Ghi danh sách đối tượng ra file CSV (kèm cột gia_ban và thanh_tien)."""
        cot = ["ma_don", "ma_sp", "ten_sp", "don_gia", "loai", "ty_le_giam",
               "ma_nv", "ho_ten", "so_luong", "ngay_ban", "gia_ban", "thanh_tien"]
        with open(duong_dan_xuat, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=cot)
            writer.writeheader()
            for dh in self.danh_sach_don_hang:
                writer.writerow(dh.to_dict())
        print(f"Da ghi {len(self.danh_sach_don_hang)} dong ra file: {duong_dan_xuat}")

    def hien_thi_tat_ca(self):
        """TH1: Hiển thị tất cả đối tượng đã đọc từ CSV."""
        print("=== TH1: HIEN THI TAT CA DON HANG ===")
        for dh in self.danh_sach_don_hang:
            print(dh)

    def hien_thi_theo_loai(self, loai):
        """TH2: Lọc đối tượng theo loại (thuong / khuyen_mai)."""
        print(f"=== TH2: DON HANG LOAI '{loai}' ===")
        ket_qua = [dh for dh in self.danh_sach_don_hang if dh.loai == loai]
        for dh in ket_qua:
            print(dh)
        return ket_qua

    def hien_thi_theo_nhan_vien(self, ma_nv):
        """TH3: Lọc đối tượng theo mã nhân viên."""
        print(f"=== TH3: DON HANG CUA NHAN VIEN '{ma_nv}' ===")
        ket_qua = [dh for dh in self.danh_sach_don_hang if dh.ma_nv == ma_nv]
        for dh in ket_qua:
            print(dh)
        return ket_qua

    def tinh_tong_thanh_tien(self):
        """TH4: Tính tổng thành tiền của tất cả đối tượng."""
        print("=== TH4: TONG THANH TIEN ===")
        tong = sum(dh.tinh_thanh_tien() for dh in self.danh_sach_don_hang)
        print(f"Tong thanh tien: {tong:,.0f} VND")
        return tong

    def tim_don_hang_theo_ma(self, ma_don):
        """TH5: Tìm đối tượng theo mã đơn hàng."""
        print(f"=== TH5: TIM DON HANG MA '{ma_don}' ===")
        for dh in self.danh_sach_don_hang:
            if dh.ma_don == ma_don:
                print(dh)
                return dh
        print(f"Khong tim thay don hang ma '{ma_don}'")
        return None

    def sap_xep_theo_thanh_tien(self, giam_dan=True):
        """TH6: Sắp xếp đối tượng theo thành tiền."""
        print("=== TH6: SAP XEP THEO THANH TIEN (GIAM DAN) ===")
        ket_qua = sorted(self.danh_sach_don_hang, key=lambda dh: dh.tinh_thanh_tien(), reverse=giam_dan)
        for dh in ket_qua:
            print(f"{dh.ma_don}  {dh.ten_sp:<20}{dh.tinh_thanh_tien():,.0f} VND")
        return ket_qua

    def thong_ke_theo_nhan_vien(self):
        """TH7: Thống kê doanh số theo từng nhân viên."""
        print("=== TH7: THONG KE DOANH SO THEO NHAN VIEN ===")
        thong_ke = {}
        for dh in self.danh_sach_don_hang:
            if dh.ma_nv not in thong_ke:
                thong_ke[dh.ma_nv] = {"ho_ten": dh.ho_ten, "tong_thanh_tien": 0, "so_don": 0}
            thong_ke[dh.ma_nv]["tong_thanh_tien"] += dh.tinh_thanh_tien()
            thong_ke[dh.ma_nv]["so_don"] += 1

        for ma_nv, info in sorted(thong_ke.items(), key=lambda x: x[1]["tong_thanh_tien"], reverse=True):
            print(f"  {ma_nv}  {info['ho_ten']:<20}{info['tong_thanh_tien']:,.0f} VND  ({info['so_don']} don)")
        return thong_ke


if __name__ == "__main__":
    # Cách 1: Tạo QuanLyDonHang bình thường
    ql = QuanLyDonHang(os.path.join(BASE_DIR, "du_lieu.csv"))

    # Cách 2: Sử dụng classmethod tao_tu_csv
    # ql = QuanLyDonHang.tao_tu_csv(os.path.join(BASE_DIR, "du_lieu.csv"))

    # TH1: Hiển thị tất cả
    ql.hien_thi_tat_ca()
    print()

    # TH2: Lọc theo loại
    ql.hien_thi_theo_loai("khuyen_mai")
    print()

    # TH3: Lọc theo nhân viên
    ql.hien_thi_theo_nhan_vien("NV01")
    print()

    # TH4: Tổng thành tiền
    ql.tinh_tong_thanh_tien()
    print()

    # TH5: Tìm theo mã đơn
    ql.tim_don_hang_theo_ma("DH03")
    print()

    # TH6: Sắp xếp theo thành tiền
    ql.sap_xep_theo_thanh_tien()
    print()

    # TH7: Thống kê theo nhân viên
    ql.thong_ke_theo_nhan_vien()
    print()

    # TH8: Ghi danh sách đối tượng ra file CSV
    ql.ghi_csv(os.path.join(BASE_DIR, "ket_qua.csv"))