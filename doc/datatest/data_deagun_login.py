TEST_CASES_LOGIN = [
    {
        "id": "TC_DN01",
        "name": "(TH1) Đăng nhập thành công với tài khoản hợp lệ",
        "username": "admin",
        "password": "admin123",
        "expect_success": True
    },
    {
        "id": "TC_DN02",
        "name": "(TH2) Đăng nhập thất bại do sai mật khẩu",
        "username": "admin",
        "password": "admin999",
        "expect_success": False
    },
    {
        "id": "TC_DN03",
        "name": "(TH3) Đăng nhập thất bại do để trống mật khẩu",
        "username": "admin",
        "password": "",
        "expect_success": False
    },
    {
        "id": "TC_DN04",
        "name": "(TH4) Đăng nhập thất bại do sai tên đăng nhập",
        "username": "manager",
        "password": "admin123",
        "expect_success": False
    },
    {
        "id": "TC_DN05",
        "name": "(TH5) Đăng nhập thất bại do để trống tên đăng nhập",
        "username": "",
        "password": "admin123",
        "expect_success": False
    }
]
