import pandas as pd
import os

class NhanVienABC:
    def __init__(self, ma_nv, ten_nv):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv

    @property
    def luong(self):
        raise NotImplementedError

    def mo_ta(self):
        raise NotImplementedError

class NhanVienKinhDoanh(NhanVienABC):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, doanh_so, ty_le_hoa_hong):
        super().__init__(ma_nv, ten_nv)
        self.luong_co_ban = luong_co_ban
        self.doanh_so = doanh_so
        self.ty_le_hoa_hong = ty_le_hoa_hong

    @property
    def luong_co_ban(self):
        return self._luong_co_ban

    @luong_co_ban.setter
    def luong_co_ban(self, value):
        value = float(value)

        if value <= 0:
            raise ValueError("Lương cơ bản phải lớn hơn 0")

        self._luong_co_ban = value

    @property
    def doanh_so(self):
        return self._doanh_so

    @doanh_so.setter
    def doanh_so(self, value):
        value = float(value)

        if value < 0:
            raise ValueError("Doanh số không được âm")

        self._doanh_so = value

    @property
    def ty_le_hoa_hong(self):
        return self._ty_le_hoa_hong

    @ty_le_hoa_hong.setter
    def ty_le_hoa_hong(self, value):
        value = float(value)

        if value < 0:
            raise ValueError("Tỷ lệ hoa hồng không được âm")

        self._ty_le_hoa_hong = value

    @property
    def luong(self):
        return (self.luong_co_ban + self.doanh_so * self.ty_le_hoa_hong / 100)

    def mo_ta(self):
        return f"Nhân viên kinh doanh: {self.ten_nv}"

    def to_dict(self):
        return {
            "ma_nv": self.ma_nv,
            "ten_nv": self.ten_nv,
            "luong_co_ban": self.luong_co_ban,
            "doanh_so": self.doanh_so,
            "ty_le_hoa_hong": self.ty_le_hoa_hong,
            "luong": self.luong
        }

    def __str__(self):
        return (
            f"{self.ma_nv:<10}"
            f"{self.ten_nv:<20}"
            f"{self.luong_co_ban:>15,.0f}"
            f"{self.doanh_so:>15,.0f}"
            f"{self.ty_le_hoa_hong:>10.2f}"
            f"{self.luong:>15,.0f}"
        )


class QuanLyNhanVien:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.DataFrame()
        self.doc_du_lieu()

    def doc_du_lieu(self):
        if os.path.exists(self.file_path):
            self.df = pd.read_csv(self.file_path, encoding="utf-8-sig")
            if "luong" not in self.df.columns:
                self.cap_nhat_luong()
        else:
            self.df = pd.DataFrame(
                columns=[
                    "ma_nv",
                    "ten_nv",
                    "luong_co_ban",
                    "doanh_so",
                    "ty_le_hoa_hong",
                    "luong"
                ]
            )

    def them_nhan_vien(self, nv):
        if not isinstance(nv, NhanVienKinhDoanh):
            raise TypeError(
                "Chỉ được thêm NhanVienKinhDoanh"
            )

        if nv.ma_nv in self.df["ma_nv"].values:
            raise ValueError(
                f"Mã nhân viên {nv.ma_nv} đã tồn tại"
            )

        self.df.loc[len(self.df)] = nv.to_dict()

        print("Đã thêm nhân viên thành công.")

    def tim_nhan_vien(self, ma_nv):
        ket_qua = self.df[self.df["ma_nv"] == ma_nv]

        return ket_qua

    def hien_thi(self):
        if self.df.empty:
            print("Danh sách nhân viên đang trống.")
            return

        print(self.df.to_string(index=False))

    def sua_nhan_vien(self, ma_nv, ten_nv=None, luong_co_ban=None, doanh_so=None, ty_le_hoa_hong=None):
        vi_tri = self.df[self.df["ma_nv"] == ma_nv].index

        if len(vi_tri) == 0:
            raise ValueError(f"Không tìm thấy nhân viên {ma_nv}")

        index = vi_tri[0]

        if ten_nv is not None:
            self.df.loc[index, "ten_nv"] = ten_nv

        if luong_co_ban is not None:
             if luong_co_ban <=0:
                raise ValueError("Lương cơ bản phải lớn hơn 0")

            self.df.loc[index,"luong_co_ban"] = luong_co_ban

        if doanh_so is not None:
            if doanh_so < 0:
                raise ValueError("Doanh số không được âm")

            self.df.loc[index, "doanh_so"] = doanh_so

        if ty_le_hoa_hong is not None:
            if ty_le_hoa_hong < 0:
                raise ValueError("Tỷ lệ hoa hồng không được âm")

            self.df.loc[index, "ty_le_hoa_hong"] = ty_le_hoa_hong

        self.cap_nhat_luong()

        print("Đã cập nhật nhân viên thành công.")

    def xoa_nhan_vien(self, ma_nv):
        vi_tri = self.df[self.df["ma_nv"] == ma_nv].index

        if len(vi_tri) == 0:
            raise ValueError(f"Không tìm thấy nhân viên {ma_nv}")

        self.df = self.df.drop(vi_tri).reset_index(drop=True)

        print("Đã xóa nhân viên thành công.")

    def cap_nhat_luong(self):
        if self.df.empty:
            return

        self.df["luong"] = (self.df["luong_co_ban"] + self.df["doanh_so"] * self.df["ty_le_hoa_hong"] / 100)

    def tong_quy_luong(self):
        return self.df["luong"].sum()

    def nhan_vien_xuat_sac_nhat(self):
        if self.df.empty:
            return None

        index = self.df["luong"].idxmax()

        return self.df.loc[index]

    def sap_xep_theo_luong(self):
        return self.df.sort_values(by="luong", ascending=False)

    def sap_xep_theo_luong_co_ban(self):
        return self.df.sort_values(by=["luong_co_ban", "ten_nv"], ascending=[True, True])

    def loc_theo_luong(self, muc_luong):
        return self.df[self.df["luong"] > muc_luong]

    def luu_du_lieu(self):
        self.df.to_csv( self.file_path, index=False, encoding="utf-8-sig")

        print("Đã lưu dữ liệu.")
