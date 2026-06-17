# Bảng Dữ Liệu Kiểm Thử (Data Test Profile BQD)

| ID | Title | Name | Phone | Expected Results |
|---|---|---|---|---|
| **01** | Cập nhật thông tin thành công | nguyenthuhang | 9876543210 | Hệ thống lưu và cập nhật thông tin mới thành công |
| **02** | Cập nhật thông tin thất bại khi nhập sai Phone | nguyenthuhang | mothai | Hệ thống hiển thị lỗi "Update failed" |
| **03** | Cập nhật thông tin thất bại khi để trống Phone | nguyenthuhang | (Trống) | Hệ thống hiển thị lỗi yêu cầu nhập Phone |
| **04** | Cập nhật thông tin thất bại khi nhập sai Name | ng uye nthuhang | mothai | Hệ thống hiển thị lỗi "Update failed" |
| **05** | Cập nhật thông tin thất bại khi để trống Name | (Trống) | mothai | Hệ thống hiển thị lỗi "Name cannot be empty" |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công (Xem file login_LTD.md).
2. **Bước 2:** Click vào menu **Profile** ở thanh điều hướng.
3. **Bước 3:** Thay đổi dữ liệu tại các trường **Name** và **Phone** theo từng test case.
4. **Bước 4:** Click **Update Profile**.
5. **Bước 5:** Đánh giá kết quả hiển thị so với **Expected Results**.
