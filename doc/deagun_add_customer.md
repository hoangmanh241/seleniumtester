### 2.2.9. Chức năng “Thêm khách hàng”

**1. Tiền điều kiện:** 
Đang ở giao diện Khách hàng, mở Form "Thông tin khách hàng".

**2. Phân tích Điều kiện và hành động:**
• C1 (Tên khách hàng): T (2-100 ký tự); F (Dưới 2 / Trên 100 ký tự); B (Bỏ trống).
• C2 (Số điện thoại): T (Hợp lệ); F (Thiếu số / Chứa chữ cái); B (Bỏ trống).
• C3 (Email): T (Đúng định dạng); F (Sai định dạng); B (Bỏ trống).
• C4 (Hạng thẻ): T, F

**3. Bảng quyết định:**
| Điều kiện / Các trường hợp | TH1 | TH2 | TH3 | TH4 | TH5 | TH6 | TH7 | TH8 |
|---|---|---|---|---|---|---|---|---|
| C1 (Tên KH) | T | T | T | T | T | T | F | B |
| C2 (SĐT) | T | T | T | T | F | B | - | - |
| C3 (Email) | T | T | F | B | - | - | - | - |
| C4 (Hạng thẻ) | T | F | - | - | - | - | - | - |
| **A1 (Lưu khách hàng)** | **T** | **F** | **F** | **F** | **F** | **F** | **F** | **F** |

**4. Kịch bản test (Test cases):**
| ID | Tiêu đề | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| TC_KH01 | (TH1) Thêm KH thành công | Tên: Lê Văn A<br>SĐT: 0912345678<br>Email: a@gmail.com | Lưu thông tin khách hàng thành công. |
| TC_KH02 | (TH8) Để trống Tên KH (B) | Tên: *(Trống)*<br>SĐT: 0912345678<br>Email: a@gmail.com | Báo lỗi: "Tên khách hàng phải từ 2 đến 100 ký tự." |
| TC_KH03 | (TH7) Tên KH < 2 ký tự (F) | Tên: A<br>SĐT: 0912345678<br>Email: a@gmail.com | Báo lỗi: "Tên khách hàng phải từ 2 đến 100 ký tự." |
| TC_KH04 | (TH7) Tên KH > 100 ký tự (F) | Tên: Chuỗi 101 ký tự<br>SĐT: 0912345678<br>Email: a@gmail.com | Báo lỗi: "Tên khách hàng phải từ 2 đến 100 ký tự." |
| TC_KH05 | (TH6) Để trống Số điện thoại (B) | Tên: Lê Văn B<br>SĐT: *(Trống)*<br>Email: b@gmail.com | Báo lỗi: "Số điện thoại không hợp lệ." |
| TC_KH06 | (TH5) Số điện thoại thiếu số (F) | Tên: Lê Văn B<br>SĐT: 0912<br>Email: b@gmail.com | Báo lỗi: "Số điện thoại không hợp lệ." |
| TC_KH07 | (TH5) Số điện thoại chứa chữ (F) | Tên: Lê Văn B<br>SĐT: 091234abcd<br>Email: b@gmail.com | Báo lỗi: "Số điện thoại không hợp lệ." |
| TC_KH08 | (TH4) Để trống Email (B) | Tên: Lê Văn C<br>SĐT: 0912345678<br>Email: *(Trống)* | Báo lỗi yêu cầu không được để trống Email. |
