TEST_CASES_PROFILE_BQD = [
    {
        "id": "01",
        "name": "Cập nhật thông tin thành công",
        "profile_name": "nguyenthuhang",
        "phone": "9876543210",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Cập nhật thông tin thất bại khi nhập sai Phone",
        "profile_name": "nguyenthuhang",
        "phone": "mothai",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Cập nhật thông tin thất bại khi để trống Phone",
        "profile_name": "nguyenthuhang",
        "phone": "",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Cập nhật thông tin thất bại khi nhập sai Name",
        "profile_name": "ng uye nthuhang",
        "phone": "mothai",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Cập nhật thông tin thất bại khi để trống Name",
        "profile_name": "",
        "phone": "mothai",
        "expect_success": False
    }
]
