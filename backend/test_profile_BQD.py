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
from data_profile_BQD import TEST_CASES_PROFILE_BQD

def login(driver, wait):
    driver.get("https://english-hub-aoe.vercel.app/pages/auth/login.html")
    
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/input[1]")))
    email_input.clear()
    email_input.send_keys("Hoangtrungmanh24@gmail.com") # Tùy chỉnh tài khoản test
    
    pwd_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
    pwd_input.clear()
    pwd_input.send_keys("24012004")
    
    login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/button[1]")
    login_btn.click()
    
    time.sleep(3)

def run_profile_test(driver, wait, data):
    print(f"\n==================================================")
    print(f"BẮT ĐẦU CHẠY: [{data['id']}] - {data['name']}")
    
    test_result = "Fail"
    is_success = False
    
    try:
        # Bước 1: Login
        login(driver, wait)
        
        # Bước 2: Nhấn vào thanh điều hướng Profile
        try:
            sidebar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div[2]/button[5]")))
            sidebar_btn.click()
            time.sleep(1)
        except Exception as e:
            print("Không tìm thấy nút Profile trên sidebar.")
            return "Fail"
            
        # Bước 3: Nhập Name
        try:
            name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[1]/input")))
            name_input.clear()
            if data['profile_name']:
                name_input.send_keys(data['profile_name'])
        except Exception as e:
            print("Lỗi khi nhập Name")
            pass
            
        # Bước 4: Nhập Phone
        try:
            phone_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[3]/input")
            phone_input.clear()
            if data['phone']:
                phone_input.send_keys(data['phone'])
        except Exception as e:
            print("Lỗi khi nhập Phone")
            pass
            
        # Bước 5: Nhấn nút Update Profile
        try:
            update_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[5]/button[1]")
            update_btn.click()
            time.sleep(2)
        except Exception as e:
            print("Không thể click nút Update Profile.")
            return "Fail"
        
        # Kiểm tra alert/kết quả hiển thị
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
            print("   [Info]: Không có Alert báo thành công/lỗi.")
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
    
    for case in TEST_CASES_PROFILE_BQD:
        status = run_profile_test(driver, wait, case)
        results.append({
            "ID": case['id'],
            "Testcase": case['name'],
            "Pass/Fail": status
        })
        
        # Xóa cookie / LocalStorage để chuẩn bị cho test case mới, force đăng nhập lại
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        
    # XUẤT FILE EXCEL
    wb = Workbook()
    ws = wb.active
    ws.title = "Profile BQD Test Report"
    
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_profile_BQD.xlsx"
    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("Profile BQD", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo Profile BQD đã được lưu tại: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
