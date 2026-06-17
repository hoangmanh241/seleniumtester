from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
from openpyxl import Workbook
import sys
import os
from html_reporter import generate_html_report

# Thêm đường dẫn tới thư mục chứa dữ liệu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'doc', 'datatest')))
from data_login_BQD import TEST_CASES_LOGIN_BQD

def run_login_test(driver, wait, data):
    print(f"\n==================================================")
    print(f"BẮT ĐẦU CHẠY: [{data['id']}] - {data['name']}")
    
    test_result = "Fail"
    is_success = False
    
    try:
        # Mở trang web
        driver.get("https://english-hub-aoe.vercel.app/pages/auth/login.html")
        
        # Bước 1: Nhập Email
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/input[1]")))
        email_input.clear()
        if data['email']:
            email_input.send_keys(data['email'])
        
        # Bước 2: Nhập Password
        pwd_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
        pwd_input.clear()
        if data['password']:
            pwd_input.send_keys(data['password'])
        
        # Bước 3: Nhấn nút Login
        login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/button[1]")
        login_btn.click()
        
        time.sleep(2)
        
        # Kiểm tra kết quả hiển thị
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"   [Alert UI]: {alert_text}")
            
            # Kiểm tra text alert
            if "success" in alert_text.lower() or "thành công" in alert_text.lower():
                is_success = True
            else:
                is_success = False
                
            alert.accept()
        except:
            # Nếu không có alert, kiểm tra url xem có chuyển sang trang chủ/dashboard không
            current_url = driver.current_url
            if "login" not in current_url.lower():
                print(f"   [Info]: Đã chuyển hướng đến {current_url} -> Đăng nhập thành công")
                is_success = True
            else:
                is_success = False

        # Đánh giá Pass/Fail
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
    
    for case in TEST_CASES_LOGIN_BQD:
        status = run_login_test(driver, wait, case)
        results.append({
            "ID": case['id'],
            "Testcase": case['name'],
            "Pass/Fail": status
        })
        
    # XUẤT FILE EXCEL
    wb = Workbook()
    ws = wb.active
    ws.title = "Login BQD Test Report"
    
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_login_BQD.xlsx"
    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = "report_login_BQD.html"
    generate_html_report("Đăng nhập BQD", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo đăng nhập BQD đã được lưu tại: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
