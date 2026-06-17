TEST_CASES_PROFILE_LTD = [
    {
        "id": "01",
        "name": "Cập nhật thông tin thành công",
        "profile_name": "nguyenthuhang",
        "phone": "9876543210",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Cập nhật thông tin không thành công khi bỏ trống trường Name",
        "profile_name": "",
        "phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Cập nhật thông tin không thành công khi nhập >25 ký tự trường Name",
        "profile_name": "nguyenthuhangnguyenthuhangg",
        "phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Cập nhật thông tin không thành công khi nhập dấu space vào trường Name",
        "profile_name": "ng uye nthuhang",
        "phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Cập nhật thông tin không thành công khi bỏ trống trường Phone",
        "profile_name": "nguyenthuhang",
        "phone": "",
        "expect_success": False
    },
    {
        "id": "06",
        "name": "Cập nhật thông tin không thành công khi nhập không đúng định dạng Phone",
        "profile_name": "nguyenthuhang",
        "phone": "mothai",
        "expect_success": False
    },
    {
        "id": "07",
        "name": "Cập nhật thông tin không thành công khi nhập space vào trường Phone",
        "profile_name": "nguyenthuhang",
        "phone": "98 765 43210",
        "expect_success": False
    },
    {
        "id": "08",
        "name": "Cập nhật thông tin không thành công khi nhập trùng Phone có trong CSDL",
        "profile_name": "nguyenthuhang",
        "phone": "9876543210",
        "expect_success": False
    },
    {
        "id": "09",
        "name": "Cập nhật thông tin không thành công khi nhập > 11 ký tự vào trường Phone",
        "profile_name": "nguyenthuhang",
        "phone": "987654321023",
        "expect_success": False
    }
]
