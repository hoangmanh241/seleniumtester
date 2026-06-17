# Bảng Dữ Liệu Kiểm Thử (Data Test Change Password BQD)

| ID | Title | Old Password | New Password | Expected Results |
|---|---|---|---|---|
| **01** | Thay đổi password thành công | 24012004 | 0123456 | Hệ thống cập nhật Password mới thành công |
| **02** | Thay đổi password không thành công nhập < 6 ký tự New Password | 24012004 | 123 | Hệ thống hiển thị lỗi "New password must be at least 6 characters" |
| **03** | Thay đổi password không thành công khi để trống New Password | 24012004 | (Trống) | Hệ thống hiển thị lỗi "Please fill all fields" |
| **04** | Thay đổi password không thành công khi nhập sai Old Password | 0123456 | 0123456 | Hệ thống hiển thị lỗi "Change password failed" |
| **05** | Thay đổi password không thành công khi để trống Old Password | (Trống) | 0123456 | Hệ thống hiển thị lỗi "Please fill all fields" |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công.
2. **Bước 2:** Click vào menu **Profile** ở thanh điều hướng.
3. **Bước 3:** Click vào button **Change Password**.
4. **Bước 4:** Nhập thông tin tại các trường **Old Password** và **New Password** theo từng test case.
5. **Bước 5:** Click button **Change Password**.
6. **Bước 6:** Đánh giá kết quả hiển thị so với **Expected Results**.
