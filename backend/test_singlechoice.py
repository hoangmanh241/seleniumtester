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
from data_singlechoice import TEST_CASES_SINGLECHOICE

def login(driver, wait):
    driver.get("https://english-hub-aoe.vercel.app/pages/auth/login.html")
    
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/input[1]")))
    email_input.clear()
    email_input.send_keys("Hoangtrungmanh24@gmail.com")
    
    pwd_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
    pwd_input.clear()
    pwd_input.send_keys("24012004")
    
    login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/button[1]")
    login_btn.click()
    
    time.sleep(3)

def run_singlechoice_test(driver, wait, data):
    print(f"\n==================================================")
    print(f"BẮT ĐẦU CHẠY: [{data['id']}] - {data['name']}")
    
    test_result = "Fail"
    is_success = False
    
    try:
        # Bước 1: Login
        login(driver, wait)
        
        # Bước 2: Nhấn vào thanh điều hướng Assignments
        try:
            sidebar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div[2]/button[3]")))
            sidebar_btn.click()
            time.sleep(1)
        except Exception as e:
            print("Không tìm thấy nút Assignments.")
            
        # Bước 3: Nhấn nút Q (Mở form thêm câu hỏi)
        try:
            btn_q = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[3]/div[3]/div[4]/button[1]")))
            btn_q.click()
            time.sleep(1)
        except Exception as e:
            print("Không tìm thấy nút Q.")
            return "Fail"
            
        # Bước 4: Nhập Question content
        try:
            q_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/input")))
            q_input.clear()
            if data['content']:
                q_input.send_keys(data['content'])
        except Exception as e:
            pass
            
        # Bước 5, 6, 7, 8: Nhập Options A, B, C, D
        try:
            opt_a_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/input[1]")
            opt_a_input.clear()
            if data['opt_a']: opt_a_input.send_keys(data['opt_a'])
            
            opt_b_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/input[2]")
            opt_b_input.clear()
            if data['opt_b']: opt_b_input.send_keys(data['opt_b'])
            
            opt_c_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/input[3]")
            opt_c_input.clear()
            if data['opt_c']: opt_c_input.send_keys(data['opt_c'])
            
            opt_d_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/input[4]")
            opt_d_input.clear()
            if data['opt_d']: opt_d_input.send_keys(data['opt_d'])
        except Exception as e:
            pass
            
        # Bước 9: Chọn Correct Answer
        try:
            if data['correct']:
                ans_select = Select(driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/select"))
                if data['correct'].upper() == 'A':
                    ans_select.select_by_index(1) # Theo document là option[2]
                elif data['correct'].upper() == 'B':
                    ans_select.select_by_index(2) # option[3]
                elif data['correct'].upper() == 'C':
                    ans_select.select_by_index(3) # option[4]
                elif data['correct'].upper() == 'D':
                    ans_select.select_by_index(4) # option[5]
                else:
                    ans_select.select_by_visible_text(data['correct'])
        except Exception as e:
            pass
            
        # Bước 10: Nhập Explanation
        try:
            exp_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[6]/input")
            exp_input.clear()
            if data['explanation']:
                exp_input.send_keys(data['explanation'])
        except:
            pass
            
        # Bước 11: Nhấn nút Create Question
        try:
            submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/button")
            submit_btn.click()
            time.sleep(2)
        except Exception as e:
            print("Không thể click nút Create Question.")
            return "Fail"
        
        # Kiểm tra alert/kết quả hiển thị
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"   [Alert UI]: {alert_text}")
            
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
    
    for case in TEST_CASES_SINGLECHOICE:
        status = run_singlechoice_test(driver, wait, case)
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
    ws.title = "Single Choice Test Report"
    
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_singlechoice.xlsx"
    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("Single Choice", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo Single Choice đã được lưu tại: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
