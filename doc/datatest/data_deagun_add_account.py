TEST_CASES_ADD_ACCOUNT = [
    {
        "id": "TC_TK01",
        "name": "(TH1) Thêm tài khoản thành công",
        "display_name": "Nguyễn Văn A",
        "username": "nguyenvana",
        "password": "123456",
        "expect_success": True
    },
    {
        "id": "TC_TK02",
        "name": "(TH10) Để trống Tên hiển thị (B)",
        "display_name": "",
        "username": "nguyenvana",
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK03",
        "name": "(TH9) Tên hiển thị < 2 ký tự (F)",
        "display_name": "A",
        "username": "nguyenvana",
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK04",
        "name": "(TH9) Tên hiển thị > 100 ký tự (F)",
        "display_name": "a"*101,
        "username": "nguyenvana",
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK05",
        "name": "(TH8) Để trống Username (B)",
        "display_name": "Nguyễn Văn A",
        "username": "",
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK06",
        "name": "(TH7) Username < 4 ký tự (F)",
        "display_name": "Nguyễn Văn A",
        "username": "abc",
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK07",
        "name": "(TH7) Username > 30 ký tự (F)",
        "display_name": "Nguyễn Văn A",
        "username": "a"*31,
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK08",
        "name": "(TH7) Username chứa ký tự cấm (F)",
        "display_name": "Nguyễn Văn A",
        "username": "nguyen van a!",
        "password": "123456",
        "expect_success": False
    },
    {
        "id": "TC_TK09",
        "name": "(TH4) Để trống Mật khẩu (B)",
        "display_name": "Nguyễn Văn A",
        "username": "nguyenvana",
        "password": "",
        "expect_success": False
    },
    {
        "id": "TC_TK10",
        "name": "(TH3) Mật khẩu < 6 ký tự (F)",
        "display_name": "Nguyễn Văn A",
        "username": "nguyenvana",
        "password": "12345",
        "expect_success": False
    }
]
