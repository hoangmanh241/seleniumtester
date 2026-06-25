# Hướng dẫn chạy bộ Test Automation cho hệ thống DEAGUN (Quản lý Nhà hàng)

## 1. Yêu cầu môi trường
- **Python**: Phiên bản 3.8 trở lên.
- **Chrome Browser**: Phiên bản mới nhất.
- **ChromeDriver**: Cài đặt tự động qua Selenium (trong bản mới) hoặc yêu cầu tải ChromeDriver tương ứng với bản Chrome hiện tại.

## 2. Cài đặt thư viện (Dependencies)
Bạn cần mở Terminal (CMD/PowerShell) tại thư mục chứa dự án và chạy các lệnh sau:
```bash
pip install selenium openpyxl
```
*(Dự án sử dụng Selenium để thao tác UI, và openpyxl để trích xuất báo cáo Excel)*

## 3. Cấu trúc thư mục hiện tại
Dự án đã được phân chia theo từng chức năng độc lập để dễ bảo trì và mở rộng:

- **doc/datatest/**: Chứa 6 file dữ liệu test tương ứng với 6 chức năng.
  - `data_deagun_login.py`
  - `data_deagun_add_table.py`
  - `data_deagun_add_menu.py`
  - `data_deagun_create_order.py`
  - `data_deagun_add_customer.py`
  - `data_deagun_add_account.py`

- **backend/**: Chứa 6 file kịch bản chạy test tương ứng.
  - `test_deagun_login.py`
  - `test_deagun_add_table.py`
  - `test_deagun_add_menu.py`
  - `test_deagun_create_order.py`
  - `test_deagun_add_customer.py`
  - `test_deagun_add_account.py`

## 4. Các lệnh chạy dự án
Bạn mở thư mục `backend/` trong Terminal và chạy từng lệnh dưới đây tương ứng với tính năng bạn muốn test:

```bash
# 1. Chạy test Đăng nhập
python test_deagun_login.py

# 2. Chạy test Thêm Bàn
python test_deagun_add_table.py

# 3. Chạy test Thêm Món (Thực đơn)
python test_deagun_add_menu.py

# 4. Chạy test Tạo Đơn Hàng
python test_deagun_create_order.py

# 5. Chạy test Thêm Khách Hàng
python test_deagun_add_customer.py

# 6. Chạy test Thêm Tài Khoản
python test_deagun_add_account.py
```

## 5. Kết quả & Báo cáo
Sau khi một kịch bản chạy xong, nó sẽ sinh ra hai loại file báo cáo ngay trong thư mục `backend/`:
- **File Excel (.xlsx)**: Phân tích các ID test case và Pass/Fail dạng bảng tính.
- **File HTML (.html)**: Báo cáo giao diện web thân thiện, có thể mở bằng bất kỳ trình duyệt nào.
Ví dụ: `report_deagun_login.xlsx` và `report_deagun_login.html`.

## 6. Lưu ý (Dự án còn thiếu gì để test mượt mà?)
- **Tài khoản Admin hợp lệ**: Các scripts 2-6 (thêm bàn, thêm món...) có một hàm `login_admin()` đang giả định thông tin là `admin` / `admin123`. Bạn có thể thay đổi trong hàm này nếu thông tin tài khoản trên hệ thống thật thay đổi.
- **Sự ổn định mạng**: Do thao tác UI trên trình duyệt nên tốc độ load trang mạng nhà bạn có thể ảnh hưởng đến kết quả `wait.until`. Nếu gặp lỗi Timeout, bạn có thể chỉnh lại biến `wait = WebDriverWait(driver, 10)` lên 15 hoặc 20 giây ở các file test.
