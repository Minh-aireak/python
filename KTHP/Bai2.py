from abc import ABC, abstractmethod
import csv

class SanPhamABC(ABC):
    def __init__(self, ma_sp, ten_sp):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp

    @property
    @abstractmethod
    def thanh_tien(self):
        pass

    @abstractmethod
    def mo_ta(self):
        pass
    
    def __str__(self):
        return f"{self.ma_sp:<7}|{self.ten_sp:<15}"

class Sach(SanPhamABC):
    def __init__(self, ma_sp, ten_sp, gia, so_luong, the_loai):
        super().__init__(ma_sp, ten_sp)
        self._gia = gia
        self._so_luong = so_luong
        self.the_loai = the_loai

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value <= 0:
            raise ValueError("Giá không được âm!")
        self._gia = value
    
    @property
    def so_luong(self):
        return self._so_luong

    @so_luong.setter
    def so_luong(self, value):
        if value <= 0:
            raise ValueError("Số lượng không được âm!")
        self._so_luong = value

    @property
    def thanh_tien(self):
        return self.gia * self.so_luong

    @staticmethod
    def format_money(value):
        return f"{value} VND"

    def __str__(self):
        return super().__str__() + f"{self.gia:<7}|{self.so_luong:<7}|{self.the_loai:<15}|{self.format_money(self.thanh_tien)}"
                    
    @classmethod
    def from_csv_row(cls, row):
        return cls(
            ma_sp = row['ma_sp'],
            ten_sp = row['ten_sp'],
            gia = row['gia'],
            so_luong = row['so_luong'],
            the_loai = row['the_loai']
        )
    
    def __lt__(self, other):
        return self.thanh_tien < other.thanh_tien

    def __gt__(self, other):
        return self.thanh_tien > other.thanh_tien

    def __eq__(self, other):
        return self.thanh_tien == other.thanh_tien

def doc_du_lieu(path)
    ds = []
    with open(path, "r", encoding = "utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            Sds.append(ach.from_csv_row(row))

    return ds

class DonHang():
    def __init__(self, ma_don_hang):
        self.ma_don_hang = ma_don_hang
        self.danh_sach_sach = []

    def them_sach(self, sach):
        if isinstance(sach, Sach):
            self.danh_sach_don_hang.append(sach)
        else:
            raise TypeError("Không phải kiểu Sách")
    
    def tong_gia_tri(self):
        return sum(sach.thanh_tien for sach in self.danh_sach_sach)

    def sach_ban_chay_nhat(self):
        if not self.danh_sach_sach:
            return None
        return max(self.danh_sach_sach)

    def sap_xep_theo_gia_tri(self):
        return sorted(self.danh_sach_sach, reverse = True)

    def __len__(self):
        return len(self.danh_sach_sach)

    def __str__(self):
        lines = [f"Đơn hàng: {self.ma_don_hang}"]
        for sach in self.danh_sach_sach:
            lines.append(str(sach))
        return "\n".join(lines)
