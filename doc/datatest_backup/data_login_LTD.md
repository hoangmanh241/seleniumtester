# Bảng Dữ Liệu Kiểm Thử (Data Test Login LTD)

| ID | Title | Email | Password | Expected Results |
|---|---|---|---|---|
| **01** | Đăng nhập vào tài khoản thành công | Hoangtrungmanh24@gmail.com | 24012004 | Đăng nhập thành công, hệ thống di chuyển vào trang chủ của website |
| **02** | Đăng nhập vào tài khoản không thành công khi bỏ trống trường Email | (Trống) | 0338424119 | Hệ thống trả về lỗi, Yêu cầu điền vào trường “Email” |
| **03** | Nhập sai định dạng Email | hang2004gmail.com | 0338424119 | Hệ thống trả về Lỗi yêu cầu nhập lại |
| **04** | Nhập không đúng Email đã được đăng ký trước đó | hangthunguyen204@gmail.com | 0338424119 | Hệ thống trả về lỗi yêu cầu nhập lại |
| **05** | Nhập khoảng trắng vào trường Email | hang2004   @gmail. com | 0338424119 | Hệ thống trả về lỗi yêu cầu nhập lại |
| **06** | Đăng nhập không thành công khi nhập sai Password đã được cấp trước đó | hang2004@gmail.com | 0338424 | Hệ thống trả về lỗi không hợp lệ yêu cầu nhập lại |
| **07** | Bỏ trống trường Password | hang2004@gmail.com | (Trống) | Hệ thống trả về lỗi yêu cầu nhập vào trường Password |
| **08** | Nhập khoảng trắng vào trường Password | hang2004@gmail.com | 03 384 24 19 | Hệ thống trả về lỗi yêu cầu nhập lại |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Truy cập vào trang đăng nhập của website.
2. **Bước 2:** Nhập dữ liệu vào các trường **[Email]** và **[Password]** (Tham khảo giá trị theo từng Test Case ở bảng trên).
3. **Bước 3:** Click nút **“Login”**.
4. **Bước 4:** So sánh kết quả hiển thị thực tế với **Expected Results**.
