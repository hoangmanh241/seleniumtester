# Bảng Dữ Liệu Kiểm Thử (Data Test Profile LTD)

| ID | Title | Name | Phone | Expected Results |
|---|---|---|---|---|
| **01** | Cập nhật thông tin thành công | nguyenthuhang | 9876543210 | Hệ thống lưu và cập nhật thông tin mới thành công |
| **02** | Cập nhật thông tin không thành công khi bỏ trống trường Name | (Trống) | 9876543210 | Hệ thống hiện thông báo popup lỗi "Name cannot be empty" |
| **03** | Cập nhật thông tin không thành công khi nhập >25 ký tự trường Name | nguyenthuhangnguyenthuhangg | 9876543210 | Hệ thống hiện thông báo lỗi "Update failed" |
| **04** | Cập nhật thông tin không thành công khi nhập dấu space vào trường Name | ng uye nthuhang | 9876543210 | Hệ thống hiện thông báo lỗi "Update failed" |
| **05** | Cập nhật thông tin không thành công khi bỏ trống trường Phone | nguyenthuhang | (Trống) | Hệ thống hiện thông báo lỗi "Update failed" |
| **06** | Cập nhật thông tin không thành công khi nhập không đúng định dạng Phone | nguyenthuhang | mothai | Hệ thống hiện thông báo lỗi "Update failed" |
| **07** | Cập nhật thông tin không thành công khi nhập space vào trường Phone | nguyenthuhang | 98 765 43210 | Hệ thống hiện thông báo lỗi "Update failed" |
| **08** | Cập nhật thông tin không thành công khi nhập trùng Phone có trong CSDL | nguyenthuhang | 9876543210 | Hệ thống hiện thông báo lỗi "Update failed" |
| **09** | Cập nhật thông tin không thành công khi nhập > 11 ký tự vào trường Phone | nguyenthuhang | 987654321023 | Hệ thống hiện thông báo lỗi "Update failed" |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công (Sử dụng Hoangtrungmanh24@gmail.com).
2. **Bước 2:** Click vào menu **Profile** ở thanh điều hướng.
3. **Bước 3:** Thay đổi dữ liệu tại các trường **Name** và **Phone** theo từng test case.
4. **Bước 4:** Click **Update Profile**.
5. **Bước 5:** Đánh giá kết quả hiển thị so với **Expected Results**.
