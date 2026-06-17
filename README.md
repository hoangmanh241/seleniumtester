# HƯỚNG DẪN HỆ THỐNG KIỂM THỬ TỰ ĐỘNG - ENGLISH HUB AOE

Tài liệu này giải thích chi tiết về cấu trúc, cách hoạt động nội bộ của từng thành phần, hướng dẫn thiết lập và cách sử dụng dự án kiểm thử tự động (Automation Test) cho trang web [English Hub AOE](https://english-hub-aoe.vercel.app/).

---

## 1. TỔNG QUAN HỆ THỐNG & SƠ ĐỒ HOẠT ĐỘNG

Dự án này giúp **tự động hóa việc kiểm tra lỗi** trên trang web English Hub AOE bằng cách kết hợp sức mạnh của **Trí tuệ nhân tạo (Gemini API)** để sinh dữ liệu kiểm thử và **Selenium WebDriver** để giả lập thao tác của người dùng trên trình duyệt Chrome.

### Sơ đồ quy trình hoạt động:

```text
 ┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
 │   1. AI Sinh Dữ Liệu   │ ───> │  2. Lưu trữ Dữ Liệu    │ ───> │  3. Chạy Selenium &    │
 │ (backend/ai_generator.py)     │ (Thư mục doc/datatest) │      │     Tự Động Hóa        │
 └────────────────────────┘      └────────────────────────┘      └─ (backend/test_*.py) ──┘
             │                               │                               │
             │ (So sánh dữ liệu)             │                               v
             v                               v                   ┌────────────────────────┐
 ┌────────────────────────────────────────────────────────┐      │  4. Xuất Báo Cáo       │
 │          5. Đánh Giá Chất Lượng Sinh Dữ Liệu           │      │  (Excel & HTML Report) │
 │              (backend/compare_data.py)                 │      └────────────────────────┘
 └────────────────────────────────────────────────────────┘
```

---

## 2. CHI TIẾT CÁCH HOẠT ĐỘNG CỦA TỪNG MỤC (INTERNAL MECHANISMS)

### 2.1. AI Sinh Dữ Liệu (`backend/ai_generator.py`)
*   **Cách thức hoạt động:** 
    *   Sử dụng API Gemini (`gemini-2.5-flash`) để tạo ra kịch bản kiểm thử dựa trên kỹ thuật kiểm thử hộp đen chuẩn (Phân vùng tương đương và Phân tích giá trị biên).
    *   Hệ thống gửi một Prompt cấu trúc đặc biệt để ràng buộc AI chỉ trả về một chuỗi định dạng JSON hợp lệ, chứa đầy đủ các trường dữ liệu được yêu cầu kèm mô tả chi tiết bằng tiếng Việt, và trường trạng thái mong đợi (`expect_success` là `True` hoặc `False`).
    *   Sau khi nhận phản hồi từ AI, script thực hiện bóc tách JSON, phân tích cú pháp (parse) thành đối tượng Python.
*   **Cơ chế Sao lưu Lịch sử (Versioning Backup):**
    *   Khi bạn yêu cầu sinh dữ liệu mới cho một tính năng đã tồn tại dữ liệu trước đó, hệ thống sẽ quét thư mục lịch sử và tự động đổi tên các file dữ liệu cũ sang định dạng phiên bản (ví dụ: `v1`, `v2`, `v3`...) rồi di chuyển chúng vào thư mục `doc/datatest/history/`. 
    *   Cơ chế này bảo vệ dữ liệu cũ, không làm mất đi các bộ test case dị biệt (Edge cases) đã được sinh trước đó.
*   **Sản phẩm đầu ra:**
    *   Ghi song song 2 file vào thư mục `doc/datatest/`: một file mã nguồn Python `.py` chứa mảng dữ liệu cấu trúc và một file báo cáo Markdown `.md` dạng bảng trực quan để rà soát.

### 2.2. Thư mục Lưu trữ Dữ liệu (`doc/datatest/`)
*   **File Python (`data_<feature_name>.py`):**
    *   Định nghĩa một danh sách (List) các Từ điển (Dictionary) chứa dữ liệu đầu vào. Ví dụ: `TEST_CASES_LOGIN_BQD = [...]`.
    *   Mảng này sẽ được các file kịch bản Selenium (`test_*.py`) trực tiếp `import` để chạy vòng lặp kiểm thử.
*   **File Markdown (`data_<feature_name>.md`):**
    *   Tự động biên dịch mảng dữ liệu JSON thành bảng hiển thị có cấu trúc đẹp mắt.
    *   Đóng vai trò là công cụ hỗ trợ cơ chế **Human-in-the-loop** (cho phép kiểm thử viên rà soát lại logic của AI bằng mắt trước khi thực thi thực tế).

### 2.3. Bộ Chạy Tự Động Selenium (`backend/test_*.py`)
*   **Cách thức hoạt động:**
    *   Khi script được khởi chạy, nó sử dụng thư viện `selenium` để mở một trình duyệt Google Chrome mới.
    *   Script nạp danh sách các test case từ tệp dữ liệu tương ứng trong `doc/datatest/`.
    *   Với mỗi test case, trình duyệt tự động truy cập vào trang chức năng, sử dụng bộ định vị **XPath** để tìm các ô nhập liệu và nút bấm, sau đó điền dữ liệu và nhấp chuột giả lập người dùng.
    *   Chờ phản hồi từ hệ thống (ví dụ: sự xuất hiện của hộp thoại thông báo Alert hoặc sự thay đổi của đường dẫn URL chuyển trang).
    *   So sánh kết quả thực tế thu được (đăng nhập thành công/thất bại) với trường `expect_success` do AI gắn thẻ. Nếu trùng khớp, test case được đánh dấu là **Pass**, ngược lại là **Fail**.

### 2.4. Hệ Thống Xuất Báo Cáo (`backend/html_reporter.py` & `backend/generate_report.py`)
*   **Báo cáo Excel (.xlsx):**
    *   Sử dụng thư viện `openpyxl` để tạo một trang tính Excel chuyên nghiệp.
    *   Tự động căn chỉnh độ rộng cột, tô màu tiêu đề cột, đóng khung viền cho các dòng dữ liệu.
    *   Các ô trạng thái được tô màu sắc trực quan (màu xanh lá chữ đậm cho **PASS**, màu đỏ chữ đậm cho **FAIL**).
*   **Báo cáo HTML (.html):**
    *   Tổng hợp thống kê số lượng test case: Tổng số, số lượng Đạt (Passed), Thất bại (Failed), Lỗi (Broken/Skipped).
    *   Sử dụng thư viện **Chart.js** để dựng biểu đồ hình tròn (Doughnut chart) động hiển thị tỷ lệ thành công trực quan.
    *   Liệt kê danh sách chi tiết kết quả chạy từng case có biểu tượng trạng thái trực quan và tích hợp hiệu ứng hover đẹp mắt.
    *   **Tự động kích hoạt:** Trình duyệt mặc định trên máy tính của bạn sẽ tự động bật lên và hiển thị báo cáo HTML ngay sau khi kịch bản chạy xong.

### 2.5. Công cụ Đánh Giá Độ Chính Xác AI (`backend/compare_data.py`)
*   **Cách thức hoạt động:**
    *   Khi AI sinh ra bộ dữ liệu mới, làm thế nào để biết nó có hoạt động đúng cấu trúc và đạt yêu cầu chất lượng hay không? Công cụ so sánh dữ liệu sẽ tự động nạp dữ liệu mới sinh ra và mang đi so khớp với tệp dữ liệu mẫu chuẩn (trong thư mục `doc/datatest_backup/`) hoặc tệp dữ liệu cũ nhất trong lịch sử sao lưu (`doc/datatest/history/`).
    *   **Kiểm tra cấu trúc (Schema Check):** Tự động phát hiện xem AI có bỏ quên trường dữ liệu nào không (như quên nhập mật khẩu) hoặc có tự sinh ra trường dữ liệu lạ không.
    *   **Kiểm tra tính hợp lệ của kiểu dữ liệu:** Xác thực xem trường `expect_success` có luôn là kiểu Boolean (`True/False`), các trường `id` và `name` có bị trống hay không.
    *   **Kiểm tra độ đa dạng (Diversity Check):** Đảm bảo AI luôn tạo ra đầy đủ cả test case mong đợi thành công (Pass) và test case thử lỗi (Fail), tránh tình trạng AI bị ảo giác và chỉ tạo ra một loại kịch bản.

---

## 3. BẢNG TRA CỨU CÁC FILE & CÂU LỆNH CHẠY THEO CHỨC NĂNG

| Chức năng | File chạy kịch bản Selenium (trong `backend/`) | File dữ liệu đầu vào (trong `doc/datatest/`) | Lệnh Sinh Dữ Liệu Bằng AI (Tự chọn số lượng) | Lệnh Đánh Giá Chất Lượng AI | Lệnh Chạy Kiểm Thử Tự Động |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Đăng nhập (Login)** | [test_login_BQD.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_login_BQD.py) | `data_login_BQD.py` | `python backend/ai_generator.py "login_BQD" "email, password" "TEST_CASES_LOGIN_BQD" -n 10` | `python backend/compare_data.py login_BQD` | `python backend/test_login_BQD.py` |
| **Đăng ký (Register)** | [test_register_BQD.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_register_BQD.py) | `data_register_BQD.py` | `python backend/ai_generator.py "register_BQD" "fullname, email, phone, password" "TEST_CASES_REGISTER_BQD" -n 12` | `python backend/compare_data.py register_BQD` | `python backend/test_register_BQD.py` |
| **Đổi mật khẩu** | [test_changepassword_BQD.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_changepassword_BQD.py) | `data_changepassword_BQD.py` | `python backend/ai_generator.py "changepassword_BQD" "old_password, new_password, confirm_password" "TEST_CASES_CHANGEPASSWORD_BQD" -n 8` | `python backend/compare_data.py changepassword_BQD` | `python backend/test_changepassword_BQD.py` |
| **Thông tin cá nhân** | [test_profile_BQD.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_profile_BQD.py) | `data_profile_BQD.py` | `python backend/ai_generator.py "profile_BQD" "fullname, phone, address" "TEST_CASES_PROFILE_BQD" -n 6` | `python backend/compare_data.py profile_BQD` | `python backend/test_profile_BQD.py` |
| **Thêm lớp học** | [test_themlop_LTD.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_themlop_LTD.py) | `data_themlop_LTD.py` | `python backend/ai_generator.py "themlop_LTD" "classname, grade" "TEST_CASES_THEMLOP_LTD" -n 5` | `python backend/compare_data.py themlop_LTD` | `python backend/test_themlop_LTD.py` |
| **Bài tập điền từ** | [test_fillblank.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_fillblank.py) | `data_fillblank.py` | `python backend/ai_generator.py "fillblank" "question, correct_answer" "TEST_CASES_FILLBLANK" -n 10` | `python backend/compare_data.py fillblank` | `python backend/test_fillblank.py` |
| **Bài tập trắc nghiệm**| [test_singlechoice.py](file:///c:/Users/admin/Desktop/ThuHang/ThuHang/backend/test_singlechoice.py) | `data_singlechoice.py` | `python backend/ai_generator.py "singlechoice" "question, optionA, optionB, optionC, optionD, correct_option" "TEST_CASES_SINGLECHOICE" -n 10` | `python backend/compare_data.py singlechoice` | `python backend/test_singlechoice.py` |

---

## 4. HƯỚNG DẪN THIẾT LẬP MÔI TRƯỜNG

### Bước 1: Cài đặt phần mềm nền tảng
1.  **Google Chrome:** Tải và cài đặt phiên bản Chrome chính thức mới nhất.
2.  **Python 3.x:** Tải và cài đặt Python (phiên bản từ 3.8 trở lên) từ trang chủ [python.org](https://www.python.org/).
    *   > [!IMPORTANT]
        > Trong quá trình cài đặt Python trên Windows, bạn **bắt buộc phải tích chọn** ô **"Add Python to PATH"** (hoặc "Add python.exe to PATH") ở phía dưới cùng giao diện cài đặt trước khi nhấn Install.

### Bước 2: Cấu hình khóa API cho AI
1.  Nhận một khóa API từ Google AI Studio.
2.  Mở tệp `.env` trong thư mục gốc của dự án.
3.  Thay thế dòng cấu hình bằng khóa của bạn:
    ```env
    GEMINI_API_KEY=khóa_api_thực_tế_của_bạn_ở_đây
    ```

### Bước 3: Tự động cài đặt các thư viện cần thiết
1.  Mở thư mục chứa dự án `ThuHang`.
2.  Nhấp đúp chuột vào tệp script **`setup.bat`**.
3.  Cửa sổ Command Prompt hiện lên và tự động tải về các thư viện bổ trợ (`selenium`, `openpyxl`, `google-generativeai`, `python-dotenv`). Khi chạy xong, hãy nhấn phím bất kỳ để đóng cửa sổ.

---

## 5. HƯỚNG DẪN SỬ DỤNG HỆ THỐNG CHI TIẾT

### PHẦN A: Hướng Dẫn Sinh Dữ Liệu Bằng AI (AI Generator)

Công cụ `ai_generator.py` hỗ trợ hai chế độ sinh dữ liệu vô cùng linh hoạt:

#### Cách 1: Chế độ tương tác từng bước (Interactive Mode - Khuyên dùng)
Bạn không cần nhớ các tham số phức tạp, chỉ cần chạy lệnh ngắn gọn sau:
```bash
python backend/ai_generator.py
```
Hệ thống sẽ chuyển sang giao diện dòng lệnh tương tác và đặt câu hỏi từng bước cho bạn:
1.  **Nhập tên tính năng** (Ví dụ: `login_BQD`)
2.  **Nhập các trường dữ liệu cần kiểm tra** (Ví dụ: `email, password`)
3.  **Nhập tên biến lưu trữ dữ liệu** (Ví dụ: `TEST_CASES_LOGIN_BQD`)
4.  **Nhập số lượng test case muốn sinh ra** (Ví dụ: `10`, hoặc chỉ cần nhấn `Enter` để chọn số lượng mặc định là `5`).

#### Cách 2: Chế độ dòng lệnh một dòng (CLI Mode - Nhanh gọn)
Bạn có thể chỉ định tất cả các tham số và số lượng trực tiếp trên một dòng lệnh bằng tham số `-n` hoặc `--num`:
```bash
python backend/ai_generator.py "Tên_Tính_Năng" "Các_Trường_Dữ_Liệu" "TÊN_BIẾN_DATA" -n <Số_Lượng>
```
*Ví dụ thực tế:*
```bash
python backend/ai_generator.py "login_BQD" "email, password" "TEST_CASES_LOGIN_BQD" -n 12
```

---

### PHẦN B: Hướng Dẫn Đánh Giá Chất Lượng AI (Compare Tool)

Khi sinh xong dữ liệu mới, bạn nên chạy công cụ `compare_data.py` để tự động đánh giá xem chất lượng dữ liệu AI vừa sinh có chuẩn xác và trùng khớp cấu trúc của dự án không.

#### Cách 1: Chạy trực tiếp và chỉ định chức năng
```bash
python backend/compare_data.py <tên_chức_năng>
```
*Ví dụ thực tế:*
```bash
python backend/compare_data.py login_BQD
```

#### Cách 2: Chạy chế độ tương tác lựa chọn
Chỉ cần chạy lệnh:
```bash
python backend/compare_data.py
```
Hệ thống sẽ liệt kê toàn bộ các tính năng hiện có dữ liệu mới để bạn gõ số thứ tự lựa chọn và hiển thị bảng đánh giá chất lượng ngay trên màn hình.

---

### PHẦN C: Hướng Dẫn Chạy Kiểm Thử Tự Động (Selenium Runner)

Sau khi dữ liệu đã được sinh thành công trong thư mục `doc/datatest/`, bạn tiến hành chạy kiểm thử tự động bằng cách gõ lệnh chạy tệp kịch bản kiểm thử:

```bash
python backend/test_<tên_chức_năng>.py
```

*Ví dụ thực tế:*
```bash
python backend/test_login_BQD.py
```

*   **Hiện tượng trên màn hình:** Trình duyệt Chrome sẽ tự động mở lên, truy cập web, tự động điền form của từng test case, gửi biểu mẫu và đóng trình duyệt khi kết thúc.
*   **Kết quả đầu ra:** 
    *   Tệp báo cáo Excel dạng bảng lưu tại: `report_<tên_chức_năng>.xlsx`.
    *   Tệp báo cáo HTML sinh động lưu tại: `report_<tên_chức_năng>.html` và tự động hiển thị trên trình duyệt của bạn.

---

## 6. KHÁC BIỆT NỔI BẬT: BẢO CHỨNG CHẤT LƯỢNG (4 LAYERS OF VALIDATION)

Để đảm bảo các testcase do AI sinh ra không bị sai lệch logic hay ảo giác (Hallucination), dự án áp dụng mô hình 4 lớp kiểm chứng:
1.  **Chỉ thị Prompt Kỹ Thuật Hộp Đen:** AI bị ép buộc phải thiết kế cả trường hợp thành công (Pass) và các trường hợp lỗi biên trị (Fail) theo quy định kiểm thử phần mềm chuyên nghiệp.
2.  **Rà soát thủ công (Human-in-the-loop):** Bản thiết kế test case được xuất ra file bảng biểu Markdown `.md` rõ ràng trước khi chạy.
3.  **Thực thi kiểm chứng chéo (Cross-Validation):** Kết quả mong đợi của AI được kiểm chứng trực tiếp với phản hồi thực tế của trang web thông qua robot Selenium. Sự sai lệch sẽ được phát hiện ngay lập tức trong báo cáo kết quả.
4.  **Kiểm thử mờ (Fuzz Testing):** Mỗi lần sinh dữ liệu, AI sẽ cung cấp các chuỗi dữ liệu ngẫu nhiên phong phú (email sai định dạng, ký tự đặc biệt, chuỗi rỗng...) giúp phát hiện những lỗi tiềm ẩn sâu trong mã nguồn trang web.

---

## 7. KHẮC PHỤC CÁC LỖI THƯỜNG GẶP

### Lỗi 1: Lệnh "python" không được nhận diện trong Terminal
*   **Nguyên nhân:** Khi cài đặt Python bạn đã quên chọn hộp kiểm *"Add Python to PATH"*.
*   **Cách sửa:** Chạy lại file cài đặt Python `.exe` đã tải về, chọn **Modify** hoặc cài đặt lại hoàn toàn và chú ý tích chọn ô **"Add Python to PATH"**.

### Lỗi 2: Báo lỗi "Selenium WebDriver Exception" / Lỗi Chrome Driver
*   **Nguyên nhân:** Phiên bản Chrome trên máy tính của bạn và thư viện Selenium không tương thích, hoặc Chrome chưa được cài đặt.
*   **Cách sửa:** Hãy cập nhật Chrome lên phiên bản mới nhất. Thư viện Selenium mới hiện tại đã tích hợp sẵn cơ chế tự động tải và quản lý ChromeDriver tương thích mà không cần cài đặt thủ công.

### Lỗi 3: Báo lỗi không tìm thấy tệp tin hoặc đường dẫn thư mục
*   **Nguyên nhân:** Chạy các tệp kịch bản từ các thư mục làm việc sai dòng lệnh.
*   **Cách sửa:** Luôn mở cửa sổ dòng lệnh tại thư mục gốc của dự án (`ThuHang`) trước khi thực hiện các câu lệnh chạy script.
