TEST_CASES_CHANGEPASSWORD_LTD = [
    {
        "id": "01",
        "name": "Thay đổi password thành công",
        "old_password": "24012004",
        "new_password": "0123456",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Thay đổi password không thành công khi nhập sai Old Password",
        "old_password": "000000",
        "new_password": "123123",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Thay đổi password không thành công khi để trống Old Password",
        "old_password": "",
        "new_password": "0123456",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Thay đổi password không thành công khi nhập space vào Old Password",
        "old_password": "24 01 20 04",
        "new_password": "0123456",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Thay đổi password không thành công nhập < 5 ký tự New Password",
        "old_password": "24012004",
        "new_password": "123",
        "expect_success": False
    },
    {
        "id": "06",
        "name": "Thay đổi password không thành công khi nhập New Password Có chứa dấu space",
        "old_password": "24012004",
        "new_password": "012 34 56",
        "expect_success": False
    },
    {
        "id": "07",
        "name": "Thay đổi password không thành công khi để trống New Password",
        "old_password": "24012004",
        "new_password": "",
        "expect_success": False
    }
]
