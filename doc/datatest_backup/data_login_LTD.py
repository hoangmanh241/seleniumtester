TEST_CASES_LOGIN_LTD = [
    {
        "id": "01",
        "name": "Đăng nhập vào tài khoản thành công",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "24012004",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Đăng nhập vào tài khoản không thành công khi bỏ trống trường Email",
        "email": "",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Nhập sai định dạng Email",
        "email": "hang2004gmail.com",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Nhập không đúng Email đã được đăng ký trước đó",
        "email": "hangthunguyen204@gmail.com",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Nhập khoảng trắng vào trường Email",
        "email": "hang2004   @gmail. com",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "06",
        "name": "Đăng nhập không thành công khi nhập sai Password đã được cấp trước đó",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "0338424",
        "expect_success": False
    },
    {
        "id": "07",
        "name": "Bỏ trống trường Password",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "",
        "expect_success": False
    },
    {
        "id": "08",
        "name": "Nhập khoảng trắng vào trường Password",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "03 384 24 19",
        "expect_success": False
    }
]
