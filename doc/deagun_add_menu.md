### 2.2.7. Chức năng “Thêm món mới”

**1. Tiền điều kiện:** 
Đang ở giao diện Quản lý thực đơn, mở Form "Thêm món ăn". Các trường không bắt buộc hiển thị mặc định.

**2. Phân tích Điều kiện và hành động:**
• C1 (Tên món - 2 đến 100 kí tự): T (Hợp lệ: 2-100 kí tự); F (Dưới 2 kí tự / Vượt > 100 kí tự / Trùng tên); B (Bỏ trống).
• C2 (Giá bán - Số > 0): T (Hợp lệ); F (Bằng 0 hoặc âm / Nhập chữ); B (Bỏ trống).

**3. Bảng quyết định:**
| Điều kiện / Các trường hợp | TH1 | TH2 | TH3 | TH4 | TH5 |
|---|---|---|---|---|---|
| C1 (Tên món) | T | T | T | F | B |
| C2 (Giá bán) | T | F | B | - | - |
| **A1 (Lưu món mới)** | **T** | **F** | **F** | **F** | **F** |

**4. Kịch bản test (Test cases):**
| ID | Tiêu đề | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| TC_TM01 | (TH1) Thêm món thành công (Hợp lệ) | Tên: Gà rán<br>Giá: 50000 | Lưu thành công. |
| TC_TM02 | (TH5) Để trống Tên món (B) | Tên: *(Trống)*<br>Giá: 50000 | Báo lỗi: "Vui lòng nhập tên món". |
| TC_TM03 | (TH4) Tên món < 2 kí tự (F) | Tên: A<br>Giá: 50000 | Báo lỗi: "Tên món phải từ 2 kí tự". |
| TC_TM04 | (TH3) Để trống Giá bán (B) | Tên: Pizza<br>Giá: *(Trống)* | Báo lỗi: "Vui lòng nhập giá bán". |
| TC_TM05 | (TH2) Giá bán < mức tối thiểu (F) | Tên: Pizza<br>Giá: 0 hoặc -5 | Báo lỗi: "Giá bán phải lớn hơn 0". |
