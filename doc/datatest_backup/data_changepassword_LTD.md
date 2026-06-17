# Bảng Dữ Liệu Kiểm Thử (Data Test Change Password LTD)

| ID | Title | Old Password | New Password | Expected Results |
|---|---|---|---|---|
| **01** | Thay đổi password thành công | 24012004 | 0123456 | Hệ thống cập nhật password mới thành công (không hiện thông báo, button ChangePassword chỉ đổi thành màu green) |
| **02** | Thay đổi password không thành công khi nhập sai Old Password | 000000 | 123123 | Change password failed |
| **03** | Thay đổi password không thành công khi để trống Old Password | (Trống) | 0123456 | Please fill all fields |
| **04** | Thay đổi password không thành công khi nhập space vào Old Password | 24 01 20 04 | 0123456 | Change password failed |
| **05** | Thay đổi password không thành công nhập < 5 ký tự New Password | 24012004 | 123 | New password must be at least 6 characters |
| **06** | Thay đổi password không thành công khi nhập New Password Có chứa dấu space | 24012004 | 012 34 56 | Change password failed |
| **07** | Thay đổi password không thành công khi để trống New Password | 24012004 | (Trống) | Please fill all fields |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công.
2. **Bước 2:** Click vào menu **Profile** ở thanh điều hướng.
3. **Bước 3:** Click vào button **Change Password**.
4. **Bước 4:** Nhập thông tin tại các trường **Old Password** và **New Password** theo từng test case.
5. **Bước 5:** Click button **Change Password**.
6. **Bước 6:** Đánh giá kết quả hiển thị so với **Expected Results**.
