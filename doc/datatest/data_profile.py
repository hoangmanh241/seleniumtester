# data_profile.py
# Dữ liệu kiểm thử cho chức năng Cập nhật Profile (Đã đồng bộ)

TEST_CASES_PROFILE = [
    {
        "id": "01",
        "name_case": "Cập nhật thông tin thành công",
        "new_name": "nguyenthuhang",
        "new_phone": "9876543210",
        "expect_success": True
    },
    {
        "id": "02",
        "name_case": "Cập nhật thông tin không thành công khi bỏ trống trường Name",
        "new_name": "",
        "new_phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "03",
        "name_case": "Cập nhật thông tin không thành công khi nhập >25 ký tự trường Name",
        "new_name": "nguyenthuhangnguyenthuhangg",
        "new_phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "04",
        "name_case": "Cập nhật thông tin không thành công khi nhập dấu space vào trường Name",
        "new_name": "ng uye nthuhang",
        "new_phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "05",
        "name_case": "Cập nhật thông tin không thành công khi bỏ trống trường Phone",
        "new_name": "nguyenthuhang",
        "new_phone": "",
        "expect_success": False
    },
    {
        "id": "06",
        "name_case": "Cập nhật thông tin không thành công khi nhập không đúng định dạng Phone",
        "new_name": "nguyenthuhang",
        "new_phone": "mothai",
        "expect_success": False
    },
    {
        "id": "07",
        "name_case": "Cập nhật thông tin không thành công khi nhập space vào trường Phone",
        "new_name": "nguyenthuhang",
        "new_phone": "98 765 43210",
        "expect_success": False
    },
    {
        "id": "08",
        "name_case": "Cập nhật thông tin không thành công khi nhập trùng Phone có trong CSDL",
        "new_name": "nguyenthuhang",
        "new_phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "09",
        "name_case": "Cập nhật thông tin không thành công khi nhập > 11 ký tự vào trường Phone",
        "new_name": "nguyenthuhang",
        "new_phone": "987654321023",
        "expect_success": False
    },
    {
        "id": "10",
        "name_case": "Cập nhật Email và Phone nhiều lần liên tiếp với dữ liệu hợp lệ",
        "updates": [
            {"name": "nguyenthuhang", "phone": "9876543210"},
            {"name": "thuhang", "phone": "022113"},
            {"name": "nguyen", "phone": "886655"}
        ],
        "expect_success": True,
        "is_multiple": True
    }
]
