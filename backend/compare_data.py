import os
import sys
import importlib.util
import argparse

# Fix lỗi in tiếng Việt trên màn hình Terminal của Windows
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def load_test_cases(file_path):
    if not os.path.exists(file_path):
        return None, None
    try:
        spec = importlib.util.spec_from_file_location("temp_data_module", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attr in dir(module):
            val = getattr(module, attr)
            if isinstance(val, list) and attr.isupper() and attr.startswith("TEST_CASES_"):
                return attr, val
        # Fallback to any uppercase list if naming is slightly different
        for attr in dir(module):
            val = getattr(module, attr)
            if isinstance(val, list) and attr.isupper():
                return attr, val
    except Exception as e:
        print(f"[!] Không thể đọc file {os.path.basename(file_path)}: {e}")
    return None, None

def get_latest_history_file(history_dir, feature_name):
    if not os.path.exists(history_dir):
        return None
    files = []
    for f in os.listdir(history_dir):
        if f.startswith(f"data_{feature_name}_v") and f.endswith(".py"):
            # Extract version number
            try:
                parts = f.split("_v")
                if len(parts) > 1:
                    version = int(parts[-1].replace(".py", ""))
                    files.append((version, os.path.join(history_dir, f)))
            except ValueError:
                continue
    if files:
        # Return the path of the file with the highest version number
        files.sort(key=lambda x: x[0], reverse=True)
        return files[0][1]
    return None

def compare_data(feature_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    datatest_dir = os.path.join(base_dir, '..', 'doc', 'datatest')
    backup_dir = os.path.join(base_dir, '..', 'doc', 'datatest_backup')
    history_dir = os.path.join(datatest_dir, 'history')

    new_file = os.path.join(datatest_dir, f"data_{feature_name}.py")
    
    # 1. Xác định file tham chiếu (Reference File)
    # Ưu tiên 1: File trong datatest_backup (Bản mẫu chuẩn gốc)
    # Ưu tiên 2: File backup gần nhất trong history (v1, v2...)
    ref_file = os.path.join(backup_dir, f"data_{feature_name}.py")
    ref_source = "Thư mục backup chuẩn (datatest_backup)"
    
    if not os.path.exists(ref_file):
        ref_file = get_latest_history_file(history_dir, feature_name)
        ref_source = "Lịch sử backup gần nhất (history/)"

    print("==========================================================")
    print(f"[*] BẮT ĐẦU ĐÁNH GIÁ CHẤT LƯỢNG AI CHO TÍNH NĂNG: {feature_name}")
    print("==========================================================")

    # 2. Kiểm tra sự tồn tại của file mới
    if not os.path.exists(new_file):
        print(f"[FAIL] Không tìm thấy file dữ liệu mới sinh tại: {new_file}")
        print("Vui lòng chạy ai_generator.py trước để sinh dữ liệu.")
        return

    # 3. Load dữ liệu từ 2 file
    new_var, new_cases = load_test_cases(new_file)
    ref_var, ref_cases = load_test_cases(ref_file)

    if not new_cases:
        print("[FAIL] File mới trống hoặc không có biến mảng testcase (dạng danh sách viết hoa).")
        return

    print(f"[+] File dữ liệu mới sinh: {os.path.basename(new_file)}")
    print(f"    - Tên biến: {new_var}")
    print(f"    - Số lượng case: {len(new_cases)}")
    print("")

    if not ref_cases:
        print(f"[WARNING] Không tìm thấy file tham chiếu mẫu ({ref_source}).")
        print("-> Chỉ thực hiện đánh giá độc lập trên bộ dữ liệu mới sinh.")
        ref_fields = None
    else:
        print(f"[+] Tìm thấy file tham chiếu: {os.path.basename(ref_file)}")
        print(f"    - Nguồn tham chiếu: {ref_source}")
        print(f"    - Số lượng case: {len(ref_cases)}")
        print("")

    # 4. Phân tích cấu trúc trường dữ liệu (Fields)
    # Lấy các trường dữ liệu trừ id, name, expect_success
    metadata_keys = {"id", "name", "expect_success"}
    
    new_sample = new_cases[0]
    new_fields = set(new_sample.keys()) - metadata_keys

    ref_fields = None
    if ref_cases:
        ref_sample = ref_cases[0]
        ref_fields = set(ref_sample.keys()) - metadata_keys

    print("--- 1. KIỂM TRA CẤU TRÚC VÀ ĐỊNH DẠNG (SCHEMA CHECK) ---")
    
    # Check 1.1: Khớp cấu trúc trường với mẫu tham chiếu
    schema_ok = True
    if ref_fields is not None:
        missing_fields = ref_fields - new_fields
        extra_fields = new_fields - ref_fields

        if missing_fields:
            print(f"[FAIL] Thiếu trường dữ liệu so với bản cũ: {list(missing_fields)}")
            schema_ok = False
        if extra_fields:
            print(f"[WARNING] Xuất hiện trường mới lạ so với bản cũ: {list(extra_fields)}")
            # Extra fields are warnings, not hard failure unless critical

        if schema_ok and not extra_fields:
            print("[PASS] Hoàn toàn trùng khớp cấu trúc các trường dữ liệu so với bản cũ.")
        elif schema_ok:
            print("[PASS] Đầy đủ các trường bắt buộc (nhưng có thêm trường mở rộng).")
    else:
        print(f"[INFO] Các trường dữ liệu sinh ra: {list(new_fields)}")

    # Check 1.2: Định dạng các trường đặc biệt
    format_ok = True
    for i, case in enumerate(new_cases):
        case_id = case.get("id", f"Case_{i+1}")
        # Kiểm tra expect_success
        if "expect_success" not in case:
            print(f"[FAIL] Test case {case_id} thiếu trường 'expect_success'!")
            format_ok = False
        elif not isinstance(case["expect_success"], bool):
            print(f"[FAIL] Test case {case_id} có trường 'expect_success' không phải kiểu Boolean (True/False) mà là: {type(case['expect_success']).__name__}")
            format_ok = False
            
        # Kiểm tra id và name
        if "id" not in case or not case["id"]:
            print(f"[WARNING] Test case số {i+1} thiếu hoặc để trống trường 'id'!")
        if "name" not in case or not case["name"]:
            print(f"[WARNING] Test case {case_id} thiếu hoặc để trống trường 'name'!")

    if format_ok:
        print("[PASS] Định dạng kiểu dữ liệu của các trường bắt buộc (id, name, expect_success) hợp lệ.")

    print("\n--- 2. ĐÁNH GIÁ CHẤT LƯỢNG NỘI DUNG (DIVERSITY CHECK) ---")
    
    # Check 2.1: Phải có cả case thành công và case thất bại
    success_cases = [c for c in new_cases if c.get("expect_success") is True]
    fail_cases = [c for c in new_cases if c.get("expect_success") is False]

    print(f"    - Số lượng case mong đợi THÀNH CÔNG (expect_success = True): {len(success_cases)}")
    print(f"    - Số lượng case mong đợi THẤT BẠI   (expect_success = False): {len(fail_cases)}")

    diversity_ok = True
    if len(success_cases) == 0:
        print("[FAIL] AI không sinh ra test case THÀNH CÔNG nào! (Cần ít nhất 1 case đúng để kiểm tra luồng chính)")
        diversity_ok = False
    if len(fail_cases) == 0:
        print("[FAIL] AI không sinh ra test case THẤT BẠI nào! (Cần các case nhập sai để kiểm thử lỗi)")
        diversity_ok = False

    if diversity_ok:
        print("[PASS] Độ đa dạng dữ liệu tốt (Đầy đủ cả luồng thành công và luồng xử lý lỗi).")

    print("\n--- 3. DANH SÁCH CHI TIẾT CÁC TEST CASE MỚI SINH ---")
    for case in new_cases:
        status_str = "SUCCESS" if case.get("expect_success") else "FAIL"
        status_color = "[✓ MONG ĐỢI ĐẠT]" if case.get("expect_success") else "[✗ MONG ĐỢI LỖI]"
        print(f"  * ID {case.get('id', '??')}: {case.get('name', 'Không có tên')} {status_color}")

    print("\n==========================================================")
    # Kết luận tổng quan
    if schema_ok and format_ok and diversity_ok:
        print("[KẾT LUẬN] AI HOẠT ĐỘNG CHÍNH XÁC! Bộ dữ liệu mới đạt chuẩn chất lượng.")
    else:
        print("[KẾT LUẬN] AI CÓ LỖI HOẶC CHẤT LƯỢNG CHƯA ĐẠT! Vui lòng kiểm tra lại các lỗi [FAIL] ở trên.")
    print("==========================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool đánh giá độ chính xác dữ liệu AI sinh ra")
    parser.add_argument("feature", nargs="?", default=None, help="Tên tính năng cần đánh giá (VD: login_BQD)")
    args = parser.parse_args()

    feature = args.feature
    if not feature:
        # Chế độ tương tác
        print("=== CHỌN TÍNH NĂNG CẦN ĐÁNH GIÁ CHẤT LƯỢNG AI ===")
        # Liệt kê các file có sẵn trong doc/datatest
        base_dir = os.path.dirname(os.path.abspath(__file__))
        datatest_dir = os.path.join(base_dir, '..', 'doc', 'datatest')
        available_features = []
        if os.path.exists(datatest_dir):
            for f in os.listdir(datatest_dir):
                if f.startswith("data_") and f.endswith(".py"):
                    feat = f.replace("data_", "").replace(".py", "")
                    available_features.append(feat)
        
        if available_features:
            print("Các tính năng hiện có dữ liệu mới:")
            for idx, feat in enumerate(available_features, 1):
                print(f"  {idx}. {feat}")
            try:
                choice = input("\nNhập số thứ tự hoặc nhập trực tiếp tên tính năng cần đánh giá: ").strip()
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(available_features):
                        feature = available_features[idx]
                    else:
                        print("[!] Lựa chọn không hợp lệ.")
                        sys.exit(1)
                else:
                    feature = choice
            except (KeyboardInterrupt, SystemExit):
                sys.exit(0)
        else:
            print("[!] Không tìm thấy dữ liệu mới nào trong thư mục doc/datatest/.")
            try:
                feature = input("Nhập tên tính năng muốn kiểm tra thủ công (VD: login_BQD): ").strip()
            except (KeyboardInterrupt, SystemExit):
                sys.exit(0)

    if feature:
        compare_data(feature)
