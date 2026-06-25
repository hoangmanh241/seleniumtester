### 2.2.6. Chức năng “Thêm bàn mới”

**1. Tiền điều kiện:** 
Đang ở giao diện Quản lý bàn, mở Form "Thêm bàn". Các trường không bắt buộc hiển thị mặc định.

**2. Phân tích Điều kiện và hành động:**
| STT | Tên điều kiện | Kí hiệu | Giá trị |
|---|---|---|---|
| 1 | Nhập Tên bàn | C1 | T (Hợp lệ: 1-50 kí tự), F (Vượt > 50 kí tự / Trùng tên), B (Bỏ trống) |
| 2 | Khu vực | C2 | T (Đã chọn), B (Bỏ trống) |
| 3 | Sức chứa | C3 | T (Hợp lệ: 1-100), F (Vượt < 1 / > 100 / Nhập chữ), B (Bỏ trống) |

**Hành động:** A1 - Lưu bàn mới (T: Thành công / F: Báo lỗi).

**3. Bảng quyết định:**
| Điều kiện / Các trường hợp | TH1 | TH2 | TH3 | TH4 | TH5 | TH6 |
|---|---|---|---|---|---|---|
| C1 (Tên bàn) | T | T | T | T | F | B |
| C2 (Khu vực) | T | T | T | B | - | - |
| C3 (Sức chứa) | T | F | B | - | - | - |
| **A1 (Lưu bàn mới)** | **T** | **F** | **F** | **F** | **F** | **F** |

**4. Kịch bản test (Test cases):**
| ID | Tiêu đề | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| TC_TB01 | (TH1) Thêm bàn thành công | Tên: Bàn 01<br>Khu vực: Tầng 1<br>Sức chứa: 4 | Lưu thành công. |
| TC_TB02 | (TH6) Để trống Tên bàn (B) | Tên: *(Trống)*<br>Khu vực: Tầng 1<br>Sức chứa: 4 | Báo lỗi: "Vui lòng nhập tên bàn". |
| TC_TB03 | (TH5) Tên bàn > 50 kí tự (F) | Tên: Chuỗi 51 kí tự<br>Khu vực: Tầng 1<br>Sức chứa: 4 | Báo lỗi: "Tên bàn tối đa 50 kí tự". |
| TC_TB04 | (TH5) Tên bàn đã tồn tại (F) | Tên: Bàn 01 *(Đã có)*<br>Khu vực: Tầng 1<br>Sức chứa: 4 | Báo lỗi: "Tên bàn đã tồn tại". |
| TC_TB05 | (TH3) Để trống Sức chứa (B) | Tên: Bàn 02<br>Khu vực: Tầng 1<br>Sức chứa: *(Trống)* | Báo lỗi: "Vui lòng nhập sức chứa". |
| TC_TB06 | (TH2) Sức chứa < mức tối thiểu (F) | Tên: Bàn 02<br>Khu vực: Tầng 1<br>Sức chứa: 0 hoặc -1 | Báo lỗi: "Sức chứa phải lớn hơn 0". |
