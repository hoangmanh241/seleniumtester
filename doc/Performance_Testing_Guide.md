# Hướng Dẫn Kiểm Thử Hiệu Năng (Performance Testing) Trang Đăng Nhập

Chào bạn, để kiểm thử hiệu năng cho URL `https://english-hub-aoe.vercel.app/pages/auth/login.html`, dưới đây là hướng dẫn chi tiết từng bước, phù hợp để bạn áp dụng vào đồ án môn học.

---

## 1. Giải thích cách kiểm thử hiệu năng bằng Selenium
Mặc dù Selenium chủ yếu dùng cho **kiểm thử chức năng (Functional Testing)**, ta vẫn có thể dùng nó để đo lường **hiệu năng ở phía người dùng cuối (Client-side Performance)**. 

Cách thức hoạt động:
- **Thời gian load trang:** Đo khoảng thời gian từ lúc trình duyệt gửi yêu cầu `driver.get(url)` cho đến khi các thành phần trên giao diện (ví dụ: ô nhập email) thực sự hiển thị và sẵn sàng tương tác.
- **Thời gian login (Response UI):** Đo khoảng thời gian từ lúc click nút "Đăng nhập" cho đến khi hệ thống trả về kết quả (thông báo alert thành công/thất bại, hoặc chuyển hướng sang trang chủ).

> [!NOTE]
> Đo bằng Selenium sẽ bao gồm cả thời gian render giao diện của trình duyệt (thực tế nhất với những gì user trải nghiệm).

---

## 2. Viết script Selenium bằng Python đo thời gian lặp nhiều lần

Dưới đây là đoạn code mẫu giúp bạn đo lường thời gian load trang và thời gian xử lý đăng nhập, chạy lặp 5 lần để lấy kết quả trung bình. Bạn có thể lưu đoạn code này thành file `test_perf_login.py` và chạy.

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perf_test_login(url, email, password):
    # Sử dụng tùy chọn headless nếu muốn chạy ngầm, nhẹ máy hơn
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # Bỏ dòng này nếu muốn nhìn thấy UI
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    
    metrics = {'load_time': 0, 'login_time': 0}
    
    try:
        # --- ĐO THỜI GIAN LOAD TRANG ---
        start_load = time.time()
        driver.get(url)
        # Chờ ô email xuất hiện
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/input[1]")))
        end_load = time.time()
        metrics['load_time'] = end_load - start_load
        
        # Điền thông tin đăng nhập
        email_input.clear()
        email_input.send_keys(email)
        
        pwd_input = driver.find_element(By.XPATH, "/html/body/div[3]/input[2]")
        pwd_input.clear()
        pwd_input.send_keys(password)
        
        login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/button[1]")
        
        # --- ĐO THỜI GIAN XỬ LÝ LOGIN ---
        start_login = time.time()
        login_btn.click()
        
        # Chờ alert thông báo kết quả hoặc chuyển trang
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        
        end_login = time.time()
        metrics['login_time'] = end_login - start_login
        
    except Exception as e:
        print(f"Lỗi trong quá trình chạy: {e}")
    finally:
        driver.quit()
        
    return metrics

def main():
    url = "https://english-hub-aoe.vercel.app/pages/auth/login.html"
    email = "toducminh2004@gmail.com"
    password = "User123!@#"
    iterations = 5 # Số lần lặp
    
    total_load_time = 0
    total_login_time = 0
    success_count = 0
    
    print(f"Bắt đầu chạy test hiệu năng {iterations} lần...")
    print("-" * 40)
    
    for i in range(iterations):
        metrics = perf_test_login(url, email, password)
        if metrics['load_time'] > 0:
            print(f"Lần {i+1} | Load trang: {metrics['load_time']:.2f}s | Xử lý Login: {metrics['login_time']:.2f}s")
            total_load_time += metrics['load_time']
            total_login_time += metrics['login_time']
            success_count += 1
            
    print("-" * 40)
    if success_count > 0:
        print("=== KẾT QUẢ TỔNG QUAN ===")
        print(f"Thời gian load trang trung bình: {total_load_time / success_count:.2f}s")
        print(f"Thời gian login trung bình:      {total_login_time / success_count:.2f}s")

if __name__ == "__main__":
    main()
```

---

## 3. Hướng dẫn giả lập nhiều người dùng (Multi-threading)

Để mô phỏng có nhiều người cùng mở trình duyệt và login cùng lúc bằng Selenium, bạn có thể dùng thư viện `concurrent.futures`. Tuy nhiên, chỉ nên mô phỏng **số lượng nhỏ (ví dụ 3-5 users)** vì mỗi luồng mở 1 trình duyệt thật sẽ ngốn rất nhiều RAM.

Ví dụ tích hợp vào code trên:
```python
import concurrent.futures

def run_concurrent_users(users_count):
    print(f"Bắt đầu giả lập {users_count} users cùng lúc...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=users_count) as executor:
        # Chạy hàm perf_test_login đồng thời
        futures = [executor.submit(perf_test_login, url, email, password) for _ in range(users_count)]
        
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            print(f"User hoàn thành - Load: {res['load_time']:.2f}s, Login: {res['login_time']:.2f}s")
```

---

## 4. Hạn chế của Selenium khi làm Performance Testing

> [!WARNING]
> Không nên dùng Selenium để test tải (Load testing) mức độ lớn (hàng trăm, hàng ngàn users).

1. **Tiêu thụ tài nguyên khổng lồ:** Việc mở 1 trình duyệt (Chrome) mất đến hàng trăm MB RAM và tốn CPU. Nếu giả lập 100 users, máy tính của bạn sẽ bị treo ngay lập tức.
2. **Nhiễu kết quả (Inconsistent):** Thời gian đo được bị ảnh hưởng rất nhiều bởi cấu hình máy tính cá nhân chạy test (CPU yếu thì render chậm) thay vì do Server phản hồi chậm.
3. **Không tạo đủ áp lực cho Server:** Vì ngốn RAM client quá lớn, bạn không thể gửi lượng request đủ nhiều để biết "ngưỡng chịu đựng" (Bottleneck) của Backend/Database.

---

## 5. Đề xuất kết hợp với JMeter / k6 (Giải pháp chuẩn)

Với đồ án chuyên nghiệp, bạn nên kết hợp 2 công cụ:
* **JMeter / k6 (Backend Load Testing):** Giả lập 100 - 1000 users. Chúng KHÔNG mở trình duyệt mà chỉ gửi thẳng các gói tin HTTP Request tới API `POST /api/auth/login`. Cách này tốn cực ít RAM, giúp ép tải Database và Server Render.
* **Selenium (Frontend Performance Testing):** Đo thời gian render DOM, thời gian chạy CSS/JS trên giao diện thực với 1 user duy nhất để xem độ mượt của UI.

---

## 6. Cách đọc và đánh giá kết quả (Metrics)

Khi chạy JMeter hoặc k6, bạn cần đọc các thông số sau:
* **Response Time (Thời gian phản hồi):** 
  * **Average:** Thời gian phản hồi trung bình.
  * **90th / 95th Percentile (Quan trọng nhất):** Nếu 95th percentile là 2s, nghĩa là 95% số request hoàn thành trong vòng 2 giây (chỉ có 5% bị chậm hơn).
* **Throughput (Thông lượng):** Số lượng request Server xử lý được trong 1 giây (Requests Per Second - RPS). Thông lượng càng cao, Server càng mạnh.
* **Error Rate (Tỷ lệ lỗi):** Tỷ lệ các request thất bại (HTTP 5xx, 4xx, hoặc Timeout). Nếu Error Rate > 1%, Server đang bắt đầu quá tải.

---

## 7. Gợi ý viết Báo Cáo Kiểm Thử Hiệu Năng (Dành cho Đồ Án Sinh Viên)

Một báo cáo chuẩn cho đồ án nên có các phần:
1. **Mục tiêu kiểm thử:** Đo lường giới hạn chịu tải của API Login và đánh giá trải nghiệm UI.
2. **Kịch bản (Test Scenarios):** 
   * *Mức cơ bản (Load Test):* 50 người dùng đăng nhập đồng thời trong 1 phút.
   * *Mức căng thẳng (Stress Test):* Tăng dần từ 50 lên 200 người dùng cho đến khi xuất hiện lỗi (Error Rate > 0%).
3. **Môi trường:** 
   * Frontend: Hosted on XYZ
   * Backend: Render (Free Tier - CPU: 0.1, RAM: 512MB).
4. **Kết quả đo đạc (Bảng/Biểu đồ):** Cung cấp các biểu đồ lấy từ JMeter/k6 hoặc số liệu trung bình từ Selenium.
5. **Đánh giá và Đề xuất (Cực kỳ ghi điểm):**

> [!CAUTION]
> **Lưu ý thực tế khi host trên Render Free Tier:** 
> Server Render miễn phí sẽ tự động "ngủ" (spin down) sau 15 phút không có request. Request ĐẦU TIÊN để đánh thức server (Cold Start) sẽ tốn tới 30-50 giây. 
> **=> Cách giải quyết trong báo cáo:** Hãy ghi rõ "Bỏ qua kết quả của lần request đầu tiên (Cold Start) để tránh sai lệch số liệu. Bắt đầu đo từ lần thứ 2 khi Server đã hoạt động ổn định." Ngoài ra, Error Rate trên Render có thể tăng vọt nếu CPU vượt quá mức quy định.
