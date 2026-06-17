import os
import sys
import json
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

# Fix lỗi in tiếng Việt trên màn hình Terminal của Windows
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "your_api_key_here":
    print("Error: GEMINI_API_KEY is not set. Please update the .env file in the root directory.")
    sys.exit(1)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

def generate_test_data(feature_name, fields_info, target_variable_name, num_cases=5):
    print(f"[*] Đang yêu cầu AI sinh dữ liệu cho tính năng: {feature_name} (Số lượng: {num_cases} cases)...")
    
    prompt = f"""
    Bạn là một chuyên gia kiểm thử phần mềm (QA Automation).
    Nhiệm vụ của bạn là tạo ra {num_cases} test case tự động cho chức năng "{feature_name}".
    Các trường dữ liệu cần kiểm tra: {fields_info}.
    
    Bạn phải sinh ra ít nhất 1 case đúng (hợp lệ) và các case còn lại là test các trường hợp lỗi (ví dụ: thiếu dữ liệu, sai định dạng, v.v.).
    Mỗi test case phải bao gồm các thông tin: "id" (từ "01" đến "{num_cases:02d}"), "name" (tên case bằng tiếng Việt), các trường dữ liệu đầu vào, và "expect_success" (True hoặc False).
    
    Chỉ trả về MỘT mảng JSON hợp lệ, không có thêm text giải thích, theo định dạng như sau:
    [
        {{
            "id": "01",
            "name": "Mô tả test case",
            "field1": "value1",
            "field2": "value2",
            "expect_success": true
        }}
    ]
    """
    
    response = model.generate_content(prompt)
    
    try:
        # Lọc text rác nếu có
        text_content = response.text
        if "```json" in text_content:
            text_content = text_content.split("```json")[1].split("```")[0].strip()
        elif "```" in text_content:
            text_content = text_content.split("```")[1].strip()
            
        test_cases = json.loads(text_content)
    except Exception as e:
        print(f"[!] Lỗi phân tích JSON từ phản hồi của AI: {e}")
        print("Phản hồi gốc:\n", response.text)
        sys.exit(1)
        
    print(f"[*] Sinh dữ liệu thành công ({len(test_cases)} cases). Đang tiến hành ghi file...")
    
    # Path to doc/datatest
    base_dir = os.path.dirname(os.path.abspath(__file__))
    datatest_dir = os.path.join(base_dir, '..', 'doc', 'datatest')
    history_dir = os.path.join(datatest_dir, 'history')
    
    if not os.path.exists(datatest_dir):
        os.makedirs(datatest_dir)
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
        
    py_filepath = os.path.join(datatest_dir, f"data_{feature_name}.py")
    md_filepath = os.path.join(datatest_dir, f"data_{feature_name}.md")
    
    # Tự động Backup file cũ thành các phiên bản v1, v2, v3... vào thư mục history/
    if os.path.exists(py_filepath) or os.path.exists(md_filepath):
        version = 1
        while True:
            backup_py = os.path.join(history_dir, f"data_{feature_name}_v{version}.py")
            backup_md = os.path.join(history_dir, f"data_{feature_name}_v{version}.md")
            if not os.path.exists(backup_py) and not os.path.exists(backup_md):
                break
            version += 1
            
        print(f"[*] Đã tồn tại dữ liệu cũ. Tiến hành cất vào thư mục history/ với tên phiên bản v{version}...")
        
        if os.path.exists(py_filepath):
            os.rename(py_filepath, backup_py)
            
        if os.path.exists(md_filepath):
            os.rename(md_filepath, backup_md)
        
    # 1. Ghi file Python
    with open(py_filepath, 'w', encoding='utf-8') as f:
        f.write(f"{target_variable_name} = [\n")
        for i, case in enumerate(test_cases):
            # Convert dictionary back to formatted python string
            # specifically handling True/False values properly
            case_str = "    {\n"
            for k, v in case.items():
                if isinstance(v, bool):
                    val_str = str(v)
                elif isinstance(v, str):
                    val_str = f'"{v}"'
                else:
                    val_str = str(v)
                case_str += f'        "{k}": {val_str},\n'
            case_str += "    }"
            if i < len(test_cases) - 1:
                case_str += ","
            case_str += "\n"
            f.write(case_str)
        f.write("]\n")
        
    # 2. Ghi file Markdown
    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Bảng Dữ Liệu Kiểm Thử ({feature_name})\n\n")
        
        # Get all keys to form table headers
        if test_cases:
            keys = list(test_cases[0].keys())
            headers = [k.capitalize().replace("_", " ") for k in keys]
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("|" + "|".join(["---"] * len(keys)) + "|\n")
            
            for case in test_cases:
                row = []
                for k in keys:
                    val = case.get(k, "")
                    if val == "":
                        val = "(Trống)"
                    row.append(str(val))
                f.write("| " + " | ".join(row) + " |\n")
                
    print(f"[+] Hoàn tất! File đã được lưu tại:")
    print(f"    - {py_filepath}")
    print(f"    - {md_filepath}")

if __name__ == "__main__":
    # Check if help command is requested
    if len(sys.argv) > 1 and (sys.argv[1] in ('-h', '--help')):
        parser = argparse.ArgumentParser(description="AI Testcase Generator")
        parser.add_argument("feature", help="Tên tính năng (VD: login_BQD)")
        parser.add_argument("fields", help="Các trường dữ liệu cần test (VD: email, password)")
        parser.add_argument("var_name", help="Tên biến chứa dữ liệu (VD: TEST_CASES_LOGIN_BQD)")
        parser.add_argument("-n", "--num", type=int, default=5, help="Số lượng test case muốn sinh ra (Mặc định: 5)")
        parser.parse_args()
        sys.exit(0)

    # Use flexible parsing where positional arguments are optional
    parser = argparse.ArgumentParser(description="AI Testcase Generator")
    parser.add_argument("feature", nargs="?", default=None, help="Tên tính năng (VD: login_BQD)")
    parser.add_argument("fields", nargs="?", default=None, help="Các trường dữ liệu cần test (VD: email, password)")
    parser.add_argument("var_name", nargs="?", default=None, help="Tên biến chứa dữ liệu (VD: TEST_CASES_LOGIN_BQD)")
    parser.add_argument("-n", "--num", type=int, default=None, help="Số lượng test case muốn sinh ra")
    
    args = parser.parse_args()
    
    feature = args.feature
    fields = args.fields
    var_name = args.var_name
    num_cases = args.num

    # Interactive inputs if arguments are not fully provided
    if not feature or not fields or not var_name:
        print("=== CẤU HÌNH AI GENERATOR (INTERACTIVE MODE) ===")
        try:
            if not feature:
                feature = input("1. Nhập tên tính năng (VD: login_BQD): ").strip()
                while not feature:
                    print("[!] Tên tính năng không được để trống.")
                    feature = input("1. Nhập tên tính năng (VD: login_BQD): ").strip()
            
            if not fields:
                fields = input("2. Nhập các trường dữ liệu cần test (VD: email, password): ").strip()
                while not fields:
                    print("[!] Các trường dữ liệu không được để trống.")
                    fields = input("2. Nhập các trường dữ liệu cần test (VD: email, password): ").strip()
            
            if not var_name:
                var_name = input("3. Nhập tên biến chứa dữ liệu (VD: TEST_CASES_LOGIN_BQD): ").strip()
                while not var_name:
                    print("[!] Tên biến không được để trống.")
                    var_name = input("3. Nhập tên biến chứa dữ liệu (VD: TEST_CASES_LOGIN_BQD): ").strip()
        except (KeyboardInterrupt, SystemExit):
            print("\n[!] Đã hủy yêu cầu.")
            sys.exit(0)

    # Interactive input for number of test cases if not specified
    if num_cases is None:
        try:
            user_input = input("4. Nhập số lượng test case muốn sinh ra (Nhấn Enter để chọn 5): ").strip()
            if user_input:
                num_cases = int(user_input)
            else:
                num_cases = 5
        except ValueError:
            print("[!] Số lượng không hợp lệ. Sử dụng mặc định: 5 cases.")
            num_cases = 5
        except (KeyboardInterrupt, SystemExit):
            print("\n[!] Đã hủy yêu cầu.")
            sys.exit(0)
            
    generate_test_data(feature, fields, var_name, num_cases)
