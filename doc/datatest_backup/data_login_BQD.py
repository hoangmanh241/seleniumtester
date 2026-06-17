TEST_CASES_LOGIN_BQD = [
    {
        "id": "01",
        "name": "Đăng nhập tài khoản thành công",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "24012004",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Đăng nhập thất bại khi nhập sai Password",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "0338424",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Đăng nhập thất bại khi để trống Password",
        "email": "Hoangtrungmanh24@gmail.com",
        "password": "",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Đăng nhập thất bại khi nhập sai Email",
        "email": "hang2004gmail.com",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Đăng nhập thất bại khi để trống Email",
        "email": "",
        "password": "24012004",
        "expect_success": False
    }
]
