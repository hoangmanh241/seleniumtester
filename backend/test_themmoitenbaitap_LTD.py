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
from data_themmoitenbaitap_LTD import TEST_CASES_THEMMOITENBAITAP_LTD

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

def run_themmoitenbaitap_test(driver, wait, data):
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
            print("Không tìm thấy nút Assignments, có thể đã ở trang này.")
            
        # Bước 3: Nhấn nút Create (Mở form thêm mới)
        try:
            create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/button[2]")))
            create_btn.click()
            time.sleep(1)
        except Exception as e:
            print("Không tìm thấy nút Create (open form).")
            return "Fail"
            
        # Bước 4: Nhập Assignments name
        try:
            name_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/input[1]")))
            name_input.clear()
            if data['assignment_name']:
                name_input.send_keys(data['assignment_name'])
        except Exception as e:
            pass
            
        # Bước 5: Nhập Question count
        try:
            count_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/input[2]")
            count_input.clear()
            if data['question_count']:
                count_input.send_keys(data['question_count'])
        except Exception as e:
            pass
            
        # Bước 6: Chọn Question type
        try:
            if data['question_type']:
                type_select = Select(driver.find_element(By.XPATH, "/html/body/div[3]/div/select"))
                if "single choice" in data['question_type'].lower():
                    type_select.select_by_index(0)
                elif "fill blank" in data['question_type'].lower():
                    type_select.select_by_index(1)
                else:
                    type_select.select_by_visible_text(data['question_type'])
        except Exception as e:
            pass
            
        # Bước 7 & 8: Open time & Close time
        try:
            if data['open_time']:
                open_time_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/input[3]")
                open_time_input.send_keys(data['open_time'])
        except:
            pass
            
        try:
            if data['close_time']:
                close_time_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/input[4]")
                close_time_input.send_keys(data['close_time'])
        except:
            pass
            
        # Bước 9: Checkbox (Show result / Show explanation)
        try:
            if "result" in data['checkbox'].lower():
                cb1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/label[1]/input")
                if not cb1.is_selected():
                    cb1.click()
            elif "explanation" in data['checkbox'].lower():
                cb2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/label[2]/input")
                if not cb2.is_selected():
                    cb2.click()
        except:
            pass
            
        # Bước 10: Nhấn nút Create (Submit form)
        try:
            submit_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button[1]")
            submit_btn.click()
            time.sleep(2)
        except Exception as e:
            print("Không thể click nút Create (Submit).")
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
            print("   [Info]: Không có Alert báo thành công/lỗi. (Giả định không có alert success = lỗi popup hoặc message trong DOM)")
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
    
    for case in TEST_CASES_THEMMOITENBAITAP_LTD:
        status = run_themmoitenbaitap_test(driver, wait, case)
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
    ws.title = "Them Moi Bai Tap LTD Report"
    
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_themmoitenbaitap_LTD.xlsx"
    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("Thêm bài tập", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo Thêm bài tập đã được lưu tại: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
