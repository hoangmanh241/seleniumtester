# Bảng Dữ Liệu Kiểm Thử (Data Test Login BQD)

| ID | Title | Email | Password | Expected Results |
|---|---|---|---|---|
| **01** | Đăng nhập tài khoản thành công | Hoangtrungmanh24@gmail.com | 24012004 | Đăng nhập thành công, hệ thống chuyển vào trang chủ website |
| **02** | Đăng nhập thất bại khi nhập sai Password | hang2004@gmail.com | 0338424 | Hệ thống hiển thị lỗi Password không đúng |
| **03** | Đăng nhập thất bại khi để trống Password | hang2004@gmail.com | (Trống) | Hệ thống hiển thị lỗi yêu cầu nhập Password |
| **04** | Đăng nhập thất bại khi nhập sai Email | hang2004gmail.com | 0338424119 | Hệ thống hiển thị lỗi Email không hợp lệ |
| **05** | Đăng nhập thất bại khi để trống Email | (Trống) | 0338424119 | Hệ thống hiển thị lỗi yêu cầu nhập Email |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Truy cập trang Login của website.
2. **Bước 2:** Nhập dữ liệu vào các trường **[Email]** và **[Password]** (Tham khảo giá trị theo từng Test Case ở bảng trên).
3. **Bước 3:** Click nút **“Login”**.
4. **Bước 4:** So sánh kết quả hiển thị thực tế với **Expected Results**.
