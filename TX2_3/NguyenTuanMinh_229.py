import csv
from abc import ABC, abstractmethod

class Xe(ABC):
    def __init__(self, ma_xe, hang, nam_san_xuat, gia_xe):
        self.ma_xe = ma_xe
        self.hang = hang
        self.nam_san_xuat = nam_san_xuat
        self.gia_xe = gia_xe

    @abstractmethod
    def hien_thi(self):
        pass

class XeMay(Xe):
    def __init__(self, ma_xe, hang, nam_san_xuat, gia_xe, dung_tich, loai_xe):
        super().__init__(ma_xe, hang, nam_san_xuat, gia_xe)
        self.dung_tich = dung_tich
        self.loai_xe = loai_xe

    def hien_thi(self):
        return (f"{self.ma_xe:<8}{self.hang:<8}{self.nam_san_xuat:<15}"
                f"{self.gia_xe:<10}{self.dung_tich:<10}{self.loai_xe:<10}")

    @staticmethod
    def tieu_de():
        return (f"{'Mã xe':<8}{'Hãng':<8}{'Năm sản xuất':<15}"
                f"{'Giá xe':<10}{'Dung tích':<10}{'Loại xe':<10}")

    @staticmethod
    def nhap_xe_may(ds_ma):
        while True:
            ma_xe = input("Mã xe: ")
            if ma_xe in ds_ma:
                print(f"Mã xe: {ma_xe} trùng. Nhập lại!")
                continue
            break

        hang = input("Hãng: ")

        while True:
            try:
                nam_san_xuat = int(input("Năm sản xuất: "))
                if nam_san_xuat < 0:
                    print("Năm sản xuất phải lớn hơn 0. Nhập lại!")
                    continue
                break
            except ValueError:
                print("Năm sản xuất không hợp lệ. Nhập lại!")
                
        while True:
            try:
                gia_xe = float(input("Giá xe: "))
                if gia_xe < 0:
                    print("Giá xe phải lớn hơn hoặc bằng 0. Nhập lại!")
                    continue
                break
            except ValueError:
                print("Giá xe không hợp lệ. Nhập lại!")

        while True:
            try:
                dung_tich = float(input("Dung tích: "))
                if dung_tich <= 0:
                    print("Giá xe phải lớn hơn 0. Nhập lại!")
                    continue
                break
            except ValueError:
                print("Năm sản xuất không hợp lệ. Nhập lại!")

        loai_xe = input("Loại xe: ")

        return XeMay(ma_xe, hang, nam_san_xuat, gia_xe, dung_tich, loai_xe)

class Gara:
    def __init__(self, ten_gara, dia_chi):
        self.ten_gara = ten_gara
        self.dia_chi = dia_chi
        self.ds_xe_may = []

    def nhap_ds_xe_may(self, n):
        for i in range(n):
            print(f"----- Nhập thông tin xe máy thứ {i + 1} -----")
            xe_may = nhap_xe_may(xm.ma_xe for xm in self.ds_xe_may)

            self.ds_xe_may.append(xe_may)

    def hien_thi(self):
        print(XeMay.tieu_de())
        for xm in self.ds_xe_may:
            print(xm.hien_thi())

    def sx(self):
        return sorted(self.ds_xe_may, key = lambda xe: (xe.nam_san_xuat, -xe.gia_xe))

if __name__ == "__main__":
    n = input("Nhập n > 3:")
    gara = Gara("Aireak", "8b Tu hoàng Hà Nội")
    
    print("-" * 20 + " Nhập thông tin danh sách xe máy gara " + "-" * 20)
    gara.nhap_ds_xe_may(n)

    print("-" * 20 + " Hiển thị " + "-" * 20)
    gara.hien_thi()

    print("-" * 20 + " Sắp xếp năm sản xuất tăng " + "-" * 20)
    ds_sx = gara.sx()
    print(XeMay.tieu_de())
    for xe in ds_sx:
        print(xe.hien_thi())
        