# Bảng Dữ Liệu Kiểm Thử (Data Test Register BQD)

| ID | Title | FullName | Email | Phone | Password | Expected Results |
|---|---|---|---|---|---|---|
| **01** | Đăng ký tài khoản thành công | hang | hang2004@gmail.com | 0338424119 | 0338424119 | Hệ thống tạo tài khoản thành công, hiển thị thông báo "Register success" |
| **02** | Đăng ký thất bại khi nhập sai Password | hang | hang2004@gmail.com | 0338424119 | 033842411903384241190 | Hệ thống hiển thị lỗi "Invalid password" |
| **03** | Đăng ký thất bại khi để trống Password | hang | hang2004@gmail.com | 0338424119 | (Trống) | Hệ thống hiển thị lỗi "Password không được để trống" |
| **04** | Đăng ký thất bại khi nhập sai Phone | hang | hang2004@gmail.com | meo | 0338424119 | Hệ thống hiển thị lỗi yêu cầu nhập đúng định dạng Phone |
| **05** | Đăng ký thất bại khi để trống Phone | hang | hang2004@gmail.com | (Trống) | 0338424119 | Hệ thống yêu cầu nhập trường Phone |
| **06** | Đăng ký thất bại khi nhập sai định dạng Email | hang | hang01 | 0338424119 | 0338424119 | Hệ thống hiển thị lỗi Email không đúng định dạng |
| **07** | Đăng ký thất bại khi để trống Email | hang | (Trống) | 0338424119 | 0338424119 | Hệ thống yêu cầu nhập Email |
| **08** | Đăng ký thất bại khi nhập FullName không hợp lệ | @!#$ | hang2004@gmail.com | 0338424119 | 0338424119 | Hệ thống hiển thị lỗi FullName không hợp lệ |
| **09** | Đăng ký thất bại khi để trống FullName | (Trống) | hang2004@gmail.com | 0338424119 | 0338424119 | Hệ thống yêu cầu nhập FullName |

---

### Chi tiết các bước thực hiện
1. **Bước 1:** Chọn chức năng “Register”.
2. **Bước 2:** Nhập dữ liệu vào các trường **[FullName]**, **[Email]**, **[Phone]**, **[Password]** (Tham khảo giá trị theo từng Test Case ở bảng trên).
3. **Bước 3:** Click nút **“Register”**.
4. **Bước 4:** So sánh kết quả thực tế với **Expected Results**.
