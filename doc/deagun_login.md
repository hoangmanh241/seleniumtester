### 2.2.5. Chức năng Đăng nhập

**1. Tiền điều kiện (Pre-conditions):**
• Hệ thống máy chủ cục bộ (Localhost) và cơ sở dữ liệu (MySQL) đang hoạt động bình thường.
• Tài khoản quản trị viên với Tên đăng nhập là `admin` và Mật khẩu là `admin123` đã được khởi tạo và cấp quyền hoạt động trong cơ sở dữ liệu.
• Người dùng (Tester) đã truy cập thành công vào giao diện Đăng nhập của hệ thống DEAGUN.

**2. Phân tích Điều kiện và hành động:**
| STT | Tên điều kiện | Kí hiệu | Giá trị |
|---|---|---|---|
| 1 | Nhập Tên đăng nhập | C1 | T (Đúng), F (Sai), B (Trống) |
| 2 | Nhập Mật khẩu | C2 | T (Đúng), F (Sai), B (Trống) |

**Hành động:**
| 1 | Hệ thống xử lý đăng nhập | A1 | T (Thành công), F (Báo lỗi/Thất bại) |
|---|---|---|---|

• C1: (T) Nhập đúng `admin` / (F) Nhập sai khác `admin`.
• C2: (T) Nhập đúng `admin123` / (F) Nhập sai khác `admin123`.

**3. Lập bảng quyết định:**
| Điều kiện / Hành động | TH1 | TH2 | TH3 | TH4 | TH5 |
|---|---|---|---|---|---|
| C1 | T | T | T | F | B |
| C2 | T | F | B | - | - |
| **Hành động hệ thống** | | | | | |
| A1 | T | F | F | F | F |

**4. Kịch bản test (Test cases):**
| ID | Tiêu đề | Mô tả kịch bản | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|---|
| TC_DN01 | (TH1) Đăng nhập thành công với tài khoản hợp lệ | 1. Nhập Tên đăng nhập hợp lệ.<br>2. Nhập Mật khẩu hợp lệ.<br>3. Nhấn "Đăng nhập". | - User: admin<br>- Pass: admin123 | Hệ thống xác thực thành công và chuyển hướng người dùng vào trang Tổng quan (Dashboard). |
| TC_DN02 | (TH2) Đăng nhập thất bại do sai mật khẩu | 1. Nhập Tên đăng nhập hợp lệ.<br>2. Nhập Mật khẩu sai.<br>3. Nhấn "Đăng nhập". | - User: admin<br>- Pass: admin999 | Hệ thống từ chối truy cập và hiển thị thông báo lỗi: “Tên đăng nhập hoặc mật khẩu không chính xác”. |
| TC_DN03 | (TH3) Đăng nhập thất bại do để trống mật khẩu | 1. Nhập Tên đăng nhập hợp lệ.<br>2. Để trống trường Mật khẩu.<br>3. Nhấn "Đăng nhập". | - User: admin<br>- Pass: *(Để trống)* | Hệ thống chặn thao tác gửi dữ liệu và hiển thị thông báo yêu cầu: “Vui lòng nhập mật khẩu”. |
| TC_DN04 | (TH4) Đăng nhập thất bại do sai tên đăng nhập | 1. Nhập Tên đăng nhập sai.<br>2. Nhập Mật khẩu đúng.<br>3. Nhấn "Đăng nhập". | - User: manager<br>- Pass: admin123 | Hệ thống từ chối truy cập và hiển thị thông báo lỗi: “Tên đăng nhập hoặc mật khẩu không chính xác”. |
| TC_DN05 | (TH5) Đăng nhập thất bại do để trống tên đăng nhập | 1. Để trống trường Tên đăng nhập.<br>2. Nhập Mật khẩu hợp lệ.<br>3. Nhấn "Đăng nhập". | - User: *(Để trống)*<br>- Pass: admin123 | Hệ thống chặn thao tác gửi dữ liệu và hiển thị thông báo yêu cầu: “Vui lòng nhập tên đăng nhập”. |
