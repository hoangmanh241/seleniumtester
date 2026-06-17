from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import openpyxl
from openpyxl import Workbook
import sys
import os
from html_reporter import generate_html_report

# Thêm đường dẫn tới thư mục chứa dữ liệu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'doc', 'datatest')))
from data_registerLTD import TEST_CASES_REGISTER

def run_register_test(driver, wait, data):
    print(f"\n==================================================")
    print(f"BẮT ĐẦU CHẠY: [{data['id']}] - {data['name']}")
    
    test_result = "Fail"
    is_success = False
    
    try:
        # Mở trang web
        driver.get("https://english-hub-aoe.vercel.app/pages/auth/login.html")
        
        # Bước 0: Click nút chuyển sang trang Register
        try:
            switch_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/form/button[2]")))
            switch_btn.click()
            time.sleep(1) # Đợi form chuyển sang đăng ký
        except Exception as e:
            print("Không tìm thấy nút chuyển Register, có thể đã ở trang Register.")

        # Bước 1: Nhập FullName
        fullname_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/input[1]")))
        fullname_input.clear()
        fullname_input.send_keys(data['fullname'])
        
        # Bước 2: Nhập Email
        email_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
        email_input.clear()
        email_input.send_keys(data['email'])
        
        # Bước 3: Nhập Phone
        phone_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[3]")
        phone_input.clear()
        phone_input.send_keys(data['phone'])
        
        # Bước 4: Nhập Password
        pwd_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[4]")
        pwd_input.clear()
        pwd_input.send_keys(data['password'])
        
        # Bước 5: Chọn vai trò
        role_select = Select(driver.find_element(By.XPATH, "/html/body/div[3]/form/select"))
        try:
            role_select.select_by_visible_text(data['role'])
        except:
            try:
                role_select.select_by_value(data['role'].lower())
            except:
                pass
        
        # Bước 6: Nhấn nút Register
        register_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/button[1]")
        register_btn.click()
        
        time.sleep(2)
        
        # XỬ LÝ ALERT
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"   [Alert UI]: {alert_text}")
            
            # Nếu text trong alert chứa "success" hoặc "thành công" thì coi như tạo tài khoản thành công
            if "success" in alert_text.lower() or "thành công" in alert_text.lower():
                is_success = True
            else:
                is_success = False
                
            alert.accept()
        except:
            # Nếu không có alert
            is_success = False

        # Đánh giá
        if is_success == data['expect_success']:
            test_result = "Pass"
            print(f"=> RESULT: PASS")
        else:
            test_result = "Fail"
            print(f"=> RESULT: FAIL (Mong đợi: {'Thành công' if data['expect_success'] else 'Báo lỗi'})")
            
    except Exception as e:
        print(f"=> LỖI THỰC THI: {str(e)[:100]}")
        try:
            driver.switch_to.alert.accept()
        except:
            pass
            
    return test_result

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    
    results = []
    
    for case in TEST_CASES_REGISTER:
        status = run_register_test(driver, wait, case)
        results.append({
            "ID": case['id'],
            "Testcase": case['name'],
            "Pass/Fail": status
        })
        
    # XUẤT FILE EXCEL
    wb = Workbook()
    ws = wb.active
    ws.title = "Register Test Report"
    
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_registerLTD.xlsx"
    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("đăng ký", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo đăng ký đã được lưu tại: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
