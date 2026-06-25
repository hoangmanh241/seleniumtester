from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openpyxl import Workbook
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
from html_reporter import generate_html_report

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'doc', 'datatest')))
from data_deagun_login import TEST_CASES_LOGIN

def run_login_test(driver, wait, data):
    print(f"\n==================================================")
    print(f"BẮT ĐẦU CHẠY: [{data['id']}] - {data['name']}")
    
    test_result = "Fail"
    is_success = False
    
    try:
        driver.get("https://deagun.dpdns.org/")
        time.sleep(2)
        driver.execute_script("localStorage.clear();")
        driver.get("https://deagun.dpdns.org/")
        time.sleep(2)
        
        nav_login_btn = wait.until(EC.element_to_be_clickable((By.ID, "navLoginBtn")))
        nav_login_btn.click()
        time.sleep(1)
        
        username_input = wait.until(EC.presence_of_element_located((By.ID, "loginUsername")))
        username_input.clear()
        if data['username']:
            username_input.send_keys(data['username'])
            
        pwd_input = driver.find_element(By.ID, "loginPassword")
        pwd_input.clear()
        if data['password']:
            pwd_input.send_keys(data['password'])
        
        login_btn = driver.find_element(By.XPATH, "//form[@id='loginForm']//button[@type='submit']")
        login_btn.click()
        
        time.sleep(2)
        
        current_url = driver.current_url
        if "dashboard.html" in current_url or "orders.html" in current_url or "tables.html" in current_url:
            is_success = True
        else:
            is_success = False
            try:
                error_msg = driver.find_element(By.ID, "loginError").text
                print(f"   [Error Msg UI]: {error_msg}")
            except:
                pass

        if is_success == data['expect_success']:
            test_result = "Pass"
            print(f"=> RESULT: PASS")
        else:
            test_result = "Fail"
            print(f"=> RESULT: FAIL")
            
    except Exception as e:
        print(f"=> LỖI THỰC THI: {str(e)[:50]}")
            
    return test_result

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    
    results = []
    
    for case in TEST_CASES_LOGIN:
        status = run_login_test(driver, wait, case)
        results.append({
            "ID": case['id'],
            "Testcase": case['name'],
            "Pass/Fail": status
        })
        
    wb = Workbook()
    ws = wb.active
    ws.title = "DEAGUN Login Report"
    ws.append(["ID", "Testcase", "Pass/Fail"])
    for r in results:
        ws.append([r['ID'], r['Testcase'], r['Pass/Fail']])
    
    report_file = "report_deagun_login.xlsx"
    wb.save(report_file)
    
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("DEAGUN - Đăng nhập", results, html_report_file)
    
    print(f"\n==================================================")
    print(f"Hoàn thành! Báo cáo đã lưu: {report_file} và {html_report_file}")
    driver.quit()

if __name__ == "__main__":
    main()
