### 2.2.10. Chức năng “Thêm tài khoản”

**1. Tiền điều kiện:** 
Đang ở giao diện Quản lý tài khoản, mở Form "Thêm tài khoản".

**2. Phân tích Điều kiện và hành động:**
• C1 (Tên hiển thị): T (2-100 ký tự); F (Dưới 2 / Trên 100); B (Bỏ trống).
• C2 (Username): T (4-30 ký tự, đúng định dạng); F (Dưới 4 / Trên 30 / Chứa ký tự cấm); B (Bỏ trống).
• C3 (Vai trò): T, F
• C4 (Mật khẩu): T (>= 6 ký tự); F (Dưới 6 ký tự); B (Bỏ trống).
• C5 (Trạng thái): T, F

**3. Bảng quyết định:**
| Điều kiện / Các trường hợp | TH1 | TH2 | TH3 | TH4 | TH5 | TH6 | TH7 | TH8 | TH9 | TH10 |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 (Tên hiển thị) | T | T | T | T | T | T | T | T | F | B |
| C2 (Username) | T | T | T | T | T | T | F | B | - | - |
| C3 (Vai trò) | T | T | T | T | F | B | - | - | - | - |
| C4 (Mật khẩu) | T | T | F | B | - | - | - | - | - | - |
| C5 (Trạng thái) | T | F | - | - | - | - | - | - | - | - |
| **A1 (Lưu tài khoản)** | **T** | **F** | **F** | **F** | **F** | **F** | **F** | **F** | **F** | **F** |

**4. Kịch bản test (Test cases):**
| ID | Tiêu đề | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| TC_TK01 | (TH1) Thêm tài khoản thành công | Tên: Nguyễn Văn A<br>User: nguyenvana<br>Pass: 123456 | Lưu tài khoản thành công. |
| TC_TK02 | (TH10) Để trống Tên hiển thị (B) | Tên: *(Trống)*<br>User: nguyenvana<br>Pass: 123456 | Báo lỗi: "Tên hiển thị phải từ 2 đến 100 ký tự." |
| TC_TK03 | (TH9) Tên hiển thị < 2 ký tự (F) | Tên: A<br>User: nguyenvana<br>Pass: 123456 | Báo lỗi: "Tên hiển thị phải từ 2 đến 100 ký tự." |
| TC_TK04 | (TH9) Tên hiển thị > 100 ký tự (F) | Tên: Chuỗi 101 ký tự<br>User: nguyenvana<br>Pass: 123456 | Báo lỗi: "Tên hiển thị phải từ 2 đến 100 ký tự." |
| TC_TK05 | (TH8) Để trống Username (B) | Tên: Nguyễn Văn A<br>User: *(Trống)*<br>Pass: 123456 | Báo lỗi: "Username 4-30 ký tự, chỉ gồm chữ, số..." |
| TC_TK06 | (TH7) Username < 4 ký tự (F) | Tên: Nguyễn Văn A<br>User: abc<br>Pass: 123456 | Báo lỗi: "Username 4-30 ký tự..." |
| TC_TK07 | (TH7) Username > 30 ký tự (F) | Tên: Nguyễn Văn A<br>User: Chuỗi 31 ký tự<br>Pass: 123456 | Báo lỗi: "Username 4-30 ký tự..." |
| TC_TK08 | (TH7) Username chứa ký tự cấm (F) | Tên: Nguyễn Văn A<br>User: nguyen van a!<br>Pass: 123456 | Báo lỗi: "Username 4-30 ký tự, chỉ gồm chữ, số..." |
| TC_TK09 | (TH4) Để trống Mật khẩu (B) | Tên: Nguyễn Văn A<br>User: nguyenvana<br>Pass: *(Trống)* | Báo lỗi: "Mật khẩu tài khoản mới phải có ít nhất 6 ký tự." |
| TC_TK10 | (TH3) Mật khẩu < 6 ký tự (F) | Tên: Nguyễn Văn A<br>User: nguyenvana<br>Pass: 12345 | Báo lỗi: "Mật khẩu tài khoản mới phải có ít nhất 6 ký tự." |
