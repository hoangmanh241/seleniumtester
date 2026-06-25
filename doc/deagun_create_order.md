### 2.2.8. Chức năng “Tạo đơn hàng mới”

**1. Tiền điều kiện:** 
Đang ở giao diện Danh sách Đơn hàng, mở form "Tạo đơn hàng mới".

**2. Phân tích Điều kiện và hành động:**
• C1 (Tên khách hàng / Số bàn): T (Hợp lệ: 2-100 kí tự); F (Dưới 2 / Vượt 100 kí tự); B (Bỏ trống).
• C2 (Tổng tiền): T (Hợp lệ: > 0); F (Bằng 0 hoặc âm / Nhập chữ); B (Bỏ trống).
• C3 (Trạng thái): T, F

**3. Bảng quyết định:**
| Điều kiện / Các trường hợp | TH1 | TH2 | TH3 | TH4 | TH5 | TH6 |
|---|---|---|---|---|---|---|
| C1 (Tên KH / Số bàn) | T | T | T | T | F | B |
| C2 (Tổng tiền) | T | T | F | B | - | - |
| C3 (Trạng thái) | T | F | - | - | - | - |
| **A1 (Tạo đơn)** | **T** | **F** | **F** | **F** | **F** | **F** |

**4. Kịch bản test (Test cases):**
| ID | Tiêu đề | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| TC_DH01 | (TH1) Tạo đơn thành công | Tên KH/Số bàn: Bàn 05<br>Tổng tiền: 150000 | Tạo đơn hàng thành công. |
| TC_DH02 | (TH6) Để trống Tên KH/Số bàn (B) | Tên KH/Số bàn: *(Trống)*<br>Tổng tiền: 150000 | Báo lỗi: "Tên KH hoặc số bàn phải từ 2 đến 100 ký tự". |
| TC_DH03 | (TH5) Tên KH/Số bàn < 2 kí tự (F) | Tên KH/Số bàn: A<br>Tổng tiền: 150000 | Báo lỗi: "Tên KH hoặc số bàn phải từ 2 đến 100 ký tự". |
| TC_DH04 | (TH5) Tên KH/Số bàn > 100 kí tự (F) | Tên KH/Số bàn: Chuỗi 101 kí tự<br>Tổng tiền: 150000 | Báo lỗi: "Tên KH hoặc số bàn phải từ 2 đến 100 ký tự". |
| TC_DH05 | (TH4) Để trống Tổng tiền (B) | Tên KH/Số bàn: Bàn 05<br>Tổng tiền: *(Trống)* | Báo lỗi: "Vui lòng nhập tổng tiền". |
| TC_DH06 | (TH3) Tổng tiền <= 0 (F) | Tên KH/Số bàn: Bàn 05<br>Tổng tiền: 0 hoặc -50 | Báo lỗi: "Tổng tiền phải lớn hơn 0". |
