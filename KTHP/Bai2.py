from abc import ABC, abstractmethod
import csv

class NhanVienABC(ABC):
    def __init__(self, ma_nv, ten_nv):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv

    @property
    @abstractmethod
    def luong(self):
        pass

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ma_nv:<15}|{self.ten_nv:<15}"

class NhanVienKinhDoanh(NhanVienABC):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, doanh_so, ty_le_hoa_hong):
        super().__init__(ma_nv, ten_nv)
        self.luong_co_ban = luong_co_ban
        self.doanh_so = doanh_so
        self.ty_le_hoa_hong = ty_le_hoa_hong 

    @property
    def luong_co_ban(self):
        return self._luong_co_ban

    @property 
    def doanh_so(self):
        return self._doanh_so

    @luong_co_ban.setter
    def luong_co_ban(self, value):
        if value <= 0:
            raise ValueError
        self._luong_co_ban = value
    
    @doanh_so.setter
    def doanh_so(self, value):
        if value < 0:
            raise ValueError
        self._doanh_so = value

    @property
    def luong(self):
        return self.luong_co_ban + self.doanh_so * self.ty_le_hoa_hong / 100

    def mo_ta(self):
        return "..."
    
    @staticmethod
    def format_money(value):
        return f"{value:,.0f} VND"

    @classmethod
    def from_csv_row(cls, row):
        return cls(
            ma_nv = row['ma_nv'],
            ten_nv = row['ten_nv'],
            luong_co_ban = float(row['luong_co_ban']),
            doanh_so = float(row['doanh_so']),
            ty_le_hoa_hong = float(row['ty_le_hoa_hong'])
        )

    def __str__(self):
        return super().__str__() + f"|{self.luong_co_ban:<15}|{self.doanh_so:<15}|{self.ty_le_hoa_hong:<15}|{self.format_money(self.luong):<15}"

    def __lt__(self, other):
        return self.luong < other.luong

    def __gt__(self, other):
        return self.luong > other.luong

    def __eq__(self, other):
        return self.luong == other.luong

def doc_du_lieu(path):
    ds = []
    with open(path, "r", encoding = "utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ds.append(NhanVienKinhDoanh.from_csv_row(row))
    return ds

class PhongKinhDoanh():
    def __init__(self, ten_phong):
        self.ten_phong = ten_phong
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self, nv):
        if isinstance (nv, NhanVienKinhDoanh):
            self.danh_sach_nhan_vien.append(nv)
        else:
            raise TypeError("Không phải kiểu 'NhanVienKinhDoanh'!!")

    def tong_quy_luong(self):
        return sum(nv.luong for nv in self.danh_sach_nhan_vien)

    def nhan_vien_xuat_sac_nhat(self):
        return max(self.danh_sach_nhan_vien)

    def sap_xep_theo_luong(self):
        return sorted(self.danh_sach_nhan_vien, key = lambda x: -x.luong)

    def __len__(self):
        return len(self.danh_sach_nhan_vien)

    def __str__(self):
        lines = [f"{'Tên phòng:':<15}{self.ten_phong}"]
        for nv in self.danh_sach_nhan_vien:
            lines.append(str(nv))
        return "\n".join(lines)

