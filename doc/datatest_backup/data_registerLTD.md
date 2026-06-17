# Bảng Dữ Liệu Kiểm Thử (Data Test Register)

| ID | Title | FullName | Email | Phone | Password | Role | Expected Results |
|---|---|---|---|---|---|---|---|
| **01** | Đăng ký tài khoản website thành công | hang | hang2004@gmail.com | 0338424119 | 0338424119 | Teacher | Tạo tài khoản thành công, hệ thống hiện popup “Register success” |
| **02** | Đăng ký tài khoản thất bại khi để trống “Email” | hang | (Trống) | 0338424119 | 0338424119 | Teacher | Hệ thống trả về lỗi, Yêu cầu điền vào trường “Email” |
| **03** | Đăng ký tài khoản thất bại khi nhập sai định dạng “Email” | hang | hang01 | 0338424119 | 0338424119 | Teacher | Hệ thống hiện thông báo không hợp lệ, yêu cầu nhập lại |
| **04** | Đăng ký tài khoản thất bại khi nhập Email trùng/ đã tồn tại trong CSDL | hang | nguyen@gmail.com | 0338424119 | 0338424119 | Teacher | Hệ thống trả về thông báo lỗi cụ thể |
| **05** | Đăng ký tài khoản thất bại khi nhập Email > 20 ký tự | hang | nguyenthuhang04122004@gmail.com | 0338424119 | 0338424119 | Teacher | Hệ thống trả về Lỗi yêu cầu nhập lại. |
| **06** | Đăng ký tài khoản thất bại khi nhập Email có chứa ký tự space | hang | hang nguyen@gmail.com | 0338424119 | 0338424119 | Teacher | Hệ thống hiện thông báo không hợp lệ, yêu cầu nhập lại |
| **07** | Đăng ký tài khoản thất bại khi bỏ qua trường “Phone” | hang | hang2004@gmail.com | (Trống) | 0338424119 | Teacher | Hệ thống trả về Lỗi yêu cầu điền vào trường “Phone” |
| **08** | Đăng ký tài khoản thất bại khi nhập ký tự chữ vào trường “Phone” | hang | hang2004@gmail.com | meo | 0338424119 | Teacher | Hệ thống hiện thông báo không hợp lệ, yêu cầu nhập lại |
| **09** | Đăng ký tài khoản thất bại khi nhập Phone trùng/ đã tồn tại trong CSDL | hang | hang2004@gmail.com | 12345678 | 0338424119 | Teacher | Hệ thống trả về thông báo lỗi cụ thể |
| **10** | Đăng ký tài khoản thất bại khi nhập > 11 ký tự số | hang | hang2004@gmail.com | 0123456789012 | 0338424119 | Teacher | Hệ thống trả về lỗi yêu cầu nhập lại |
| **11** | Đăng ký tài khoản thất bại khi nhập > 20 ký tự vào trường Password | hang | hang2004@gmail.com | 0338424119 | 033842411903384241190 | Teacher | Hệ thống trả về Lỗi yêu cầu điền vào trường “Password” |
| **12** | Đăng ký tài khoản thất bại khi bỏ qua trường Password | hang | hang2004@gmail.com | 0338424119 | (Trống) | Teacher | Hệ thống trả về Lỗi yêu cầu điền vào trường “Password” |
| **13** | Đăng ký tài khoản thất bại khi nhập “Password” có chứa space | hang | hang2004@gmail.com | 0338424119 | 0338424  119 | Teacher | Hệ thống hiện thông báo không hợp lệ, yêu cầu nhập lại |
| **14** | Đăng ký tài khoản thất bại khi nhập space (khoảng trắng) vào trường FullName | thu  hang | hang2004@gmail.com | 0338424119 | 0338424119 | Teacher | Hệ thống hiện thông báo không hợp lệ, yêu cầu nhập lại |
| **15** | Đăng ký tài khoản thất bại khi nhập ký tự số/ ký tự đặc biệt vào trường FullName | @!#$ | hang2004@gmail.com | 0338424119 | 0338424119 | Teacher | Hệ thống hiện thông báo không hợp lệ, yêu cầu nhập lại |
| **16** | Đăng ký tài khoản thất bại khi nhập Full Name > 25 ký tự | hangthunguyenhangnguyenthu | hang2004@gmail.com | 0338424119 | 0338424119 | Teacher | Hệ thống trả về Lỗi, Name nằm trong khoảng 1-25 ký tự. |
| **17** | Đăng ký tài khoản thất bại khi bỏ trống cả 4 trường | (Trống) | (Trống) | (Trống) | (Trống) | Teacher | Hệ thống trả về Lỗi, yêu cầu nhập đầy đủ thông tin vào 4 trường |

---

### Chi tiết các bước thực hiện (Dùng chung cho tất cả các kịch bản)
1. **Bước 1:** Chọn Đăng ký tài khoản
2. **Bước 2:** Nhập dữ liệu vào các trường **[FullName]**, **[Email]**, **[Phone]**, **[Password]** (Tham khảo giá trị theo từng Test Case ở bảng trên).
3. **Bước 3:** Chọn Role (Teacher hoặc Student).
4. **Bước 4:** Click nút **“Register”** (hoặc “Create”).
5. **Bước 5:** So sánh kết quả thực tế với **Expected Results**.
