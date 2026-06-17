from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import time
from openpyxl import Workbook
import sys
import os
from html_reporter import generate_html_report

# Thêm đường dẫn tới thư mục chứa dữ liệu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'doc', 'datatest')))
from data_changepassword_LTD import TEST_CASES_CHANGEPASSWORD_LTD

def login(driver, wait, password):
    """
    Hàm đăng nhập. Tham số password được truyền vào vì password có thể bị đổi trong quá trình test.
    """
    driver.get("https://english-hub-aoe.vercel.app/pages/auth/login.html")
    
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/input[1]")))
    email_input.clear()
    email_input.send_keys("Hoangtrungmanh24@gmail.com") # User test mặc định
    
    pwd_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
    pwd_input.clear()
    pwd_input.send_keys(password)
    
    login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/button[1]")
    login_btn.click()
    time.sleep(3)

def revert_password(driver, wait, current_password, original_password):
    """
    Hàm dùng để tự động đổi lại password về trạng thái ban đầu (original_password)
    """
    print(f"   [Revert]: Đang khôi phục lại mật khẩu gốc ({original_password})...")
    try:
        # Khi đổi mật khẩu thành công, tài khoản có thể bị hệ thống tự động đăng xuất.
        # Xóa cookie và đăng nhập lại bằng MẬT KHẨU MỚI để thực hiện khôi phục
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        
        login(driver, wait, current_password)
        
        # Nhấn vào sidebar Profile
        sidebar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div[2]/button[5]")))
        sidebar_btn.click()
        time.sleep(1)
        
        # Nhấn vào button Change Password ở trang profile
        open_change_pw_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[5]/button[2]")))
        open_change_pw_btn.click()
        time.sleep(1)
        
        # Nhập Old Password (mật khẩu đang bị đổi)
        old_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div[1]/input")))
        old_input.clear()
        old_input.send_keys(current_password)
        
        # Nhập New Password (mật khẩu gốc cần phục hồi)
        new_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[2]/input")
        new_input.clear()
        new_input.send_keys(original_password)
        
        # Nhấn submit Change Password
        # Ưu tiên tìm text
        try:
            submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Change Password') and not(contains(@class, 'secondary'))]")
            submit_btn.click()
        except:
            submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
            submit_btn.click()
            
        time.sleep(2)
        
        # Accept thông báo alert nếu có
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass
            
        print("   [Revert]: Khôi phục mật khẩu gốc THÀNH CÔNG!")
    except Exception as e:
        print(f"   [Revert LỖI]: Không thể tự động khôi phục mật khẩu. Lỗi: {str(e)[:100]}")

def run_changepassword_test(driver, wait, data):
    print(f"\n==================================================")
    print(f"BẮT ĐẦU CHẠY: [{data['id']}] - {data['name']}")
    
    test_result = "Fail"
    is_success = False
    
    # Mật khẩu luôn bắt đầu từ 24012004 (hoặc lấy từ data nếu cần)
    # Tuy nhiên ta dùng 24012004 là mốc cố định cho các case này.
    original_password = "24012004" 
    
    try:
        # Bước 1: Login với mật khẩu hiện tại
        login(driver, wait, original_password)
        
        # Bước 2: Nhấn vào thanh điều hướng Profile
        try:
            sidebar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/div[2]/button[5]")))
            sidebar_btn.click()
            time.sleep(1)
        except Exception as e:
            print("Không tìm thấy nút Profile trên sidebar.")
            return "Fail"
            
        # Bước 3: Nhấn vào button Change Password
        try:
            open_change_pw_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[5]/button[2]")))
            open_change_pw_btn.click()
            time.sleep(1)
        except Exception as e:
            print("Không thể mở form Change Password.")
            return "Fail"
            
        # Bước 4: Nhập Old Password
        try:
            old_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/form/div[1]/input")))
            old_input.clear()
            if data['old_password']:
                old_input.send_keys(data['old_password'])
        except Exception as e:
            print("Lỗi khi nhập Old Password")
            pass
            
        # Bước 5: Nhập New Password
        try:
            new_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[2]/input")
            new_input.clear()
            if data['new_password']:
                new_input.send_keys(data['new_password'])
        except Exception as e:
            print("Lỗi khi nhập New Password")
            pass
            
        # Bước 6: Click button Change Password (Submit)
        try:
            # Ưu tiên lấy theo xpath file MD, hoặc text button
            try:
                submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Change Password') and not(contains(@class, 'secondary'))]")
            except:
                submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
                
            submit_btn.click()
            time.sleep(2)
        except Exception as e:
            print("Không thể click nút Submit Change Password.")
            return "Fail"
        
        # Kiểm tra Alert hoặc kết quả trả về
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"   [Alert UI]: {alert_text}")
            
            # Đánh giá thành công hay thất bại dựa trên test case
            # Testcase 01: Hệ thống KHÔNG hiện thông báo báo lỗi (tức là không văng lỗi)
            # Theo Requirement thì khi thành công "không hiện thông báo, button thành màu xanh"
            # Nhưng thực tế nếu có alert thì ta lấy alert.
            if "success" in alert_text.lower() or "thành công" in alert_text.lower():
                is_success = True
            else:
                is_success = False
            
            alert.accept()
        except:
            print("   [Info]: Không có Alert popup.")
            # Kiểm tra xem button có đổi màu xanh (thành công) hay form báo lỗi
            # Có thể kiểm tra url hay element. Giả định nếu không có alert lỗi thì có thể là thành công
            # Kiểm tra xem có text báo lỗi trên body không
            body_text = driver.find_element(By.TAG_NAME, "body").text
            if "failed" in body_text.lower() or "please fill" in body_text.lower() or "must be at least" in body_text.lower():
                is_success = False
            else:
                is_success = True
                
        # Đánh giá Pass/Fail
        if is_success == data['expect_success']:
            test_result = "Pass"
            print(f"=> RESULT: PASS")
            
            # => ĐẶC BIỆT: NẾU ĐÂY LÀ CASE ĐỔI PASSWORD THÀNH CÔNG, TA PHẢI REVERT LẠI
            if is_success:
                revert_password(driver, wait, current_password=data['new_password'], original_password=original_password)
                
        else:
            test_result = "Fail"
            print(f"=> RESULT: FAIL (Mong đợi: {'Thành công' if data['expect_success'] else 'Báo lỗi'})")
            
            # => ĐỀ PHÒNG CASE BỊ FAIL NHƯNG LẠI LỠ ĐỔI PASSWORD (Lỗi hệ thống), ta có thể thử khôi phục lại
            if data['expect_success'] == False and is_success == True:
                revert_password(driver, wait, current_password=data['new_password'], original_password=original_password)
                
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
    
    for case in TEST_CASES_CHANGEPASSWORD_LTD:
        status = run_changepassword_test(driver, wait, case)
        results.append({
            "ID": case['id'],
            "Testcase": case['name'],
            "Pass/Fail": status
        })
        
        # Xóa cookie / LocalStorage để chuẩn bị cho test case mới, force đăng nhập lại
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        
    # XUẤT FILE EXCEL BÁO CÁO
    wb = Workbook()
    ws = wb.active
    ws.title = "Change Password LTD Report"
    
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_changepassword_LTD.xlsx"
    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("Change Password", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo Change Password đã được lưu tại: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
