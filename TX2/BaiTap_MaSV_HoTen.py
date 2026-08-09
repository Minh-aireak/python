import os
import pandas as pd

class QuanLyBanHang:
    def __init__(self, ten_cua_hang, duong_dan_csv):
        self.ten_cua_hang = ten_cua_hang
        self.df = pd.read_csv(duong_dan_csv)

    @staticmethod
    def format_money(value):
        return f"{value:,.0f} VND"

    def tinh_gia_ban(self):
        self.df["gia_ban"] = self.df.apply(
            lambda r: r["don_gia"] * (1 - r["ty_le_giam"])
            if r["loai"] == "khuyen_mai" else r["don_gia"],
            axis=1,
        )
        return self.df["gia_ban"]

    def tinh_thanh_tien(self):
        """Thành tiền = so_luong * gia_ban."""
        self.df["thanh_tien"] = self.df["so_luong"] * self.df["gia_ban"]
        return self.df["thanh_tien"]

    def tong_doanh_thu(self):
        """Tổng doanh thu toàn cửa hàng."""
        return self.df["thanh_tien"].sum()

    def doanh_so_theo_nhan_vien(self):
        """groupby + sort_values: doanh số từng nhân viên giảm dần."""
        return (
            self.df.groupby(["ma_nv", "ho_ten"])["thanh_tien"]
            .sum().reset_index()
            .sort_values("thanh_tien", ascending=False)
        )

    def nhan_vien_xuat_sac(self):
        """Nhân viên có doanh số cao nhất."""
        ds = self.doanh_so_theo_nhan_vien()
        return ds.iloc[0]

    def don_hang_theo_gia_tri(self):
        return self.df.sort_values("thanh_tien", ascending=False)

    def thong_ke(self):
        """Tạo báo cáo tóm tắt."""
        self.tinh_gia_ban()
        self.tinh_thanh_tien()

        dong = []
        dong.append(f"BAO CAO CUA HANG: {self.ten_cua_hang}")
        dong.append("=" * 50)
        dong.append(f"Tong doanh thu: {self.format_money(self.tong_doanh_thu())}")

        dong.append("\nDoanh so tung nhan vien:")
        for _, r in self.doanh_so_theo_nhan_vien().iterrows():
            dong.append(f"  {r['ma_nv']}  {r['ho_ten']:<20}{self.format_money(r['thanh_tien'])}")

        nv = self.nhan_vien_xuat_sac()
        dong.append(f"\nNhan vien xuat sac: {nv['ho_ten']} ({self.format_money(nv['thanh_tien'])})")

        dong.append("\nDon hang theo gia tri giam dan:")
        for _, r in self.don_hang_theo_gia_tri().iterrows():
            dong.append(f"  {r['ma_don']}  {r['ten_sp']:<20}{self.format_money(r['thanh_tien'])}")

        return "\n".join(dong)


if __name__ == "__main__":
    ql = QuanLyBanHang("Cua Hang ABC", os.path.join(BASE_DIR, "du_lieu.csv"))

    # Xuất báo cáo ra màn hình + file
    bao_cao = ql.thong_ke()
    print(bao_cao)
    with open(os.path.join(BASE_DIR, "bao_cao.txt"), "w", encoding="utf-8") as f:
        f.write(bao_cao)

    print("\n(Da ghi bao cao ra bao_cao.txt)")

    # Đối chiếu nhanh bằng pandas trực tiếp
    print("\n=== XU LY BANG PANDAS ===")
    ql.tinh_gia_ban()
    ql.tinh_thanh_tien()
    print(ql.df[["ma_don", "ten_sp", "gia_ban", "so_luong", "thanh_tien"]].to_string(index=False))