TEST_CASES_REGISTER_BQD = [
    {
        "id": "01",
        "name": "Đăng ký tài khoản thành công",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Đăng ký thất bại khi nhập sai Password",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004240120040",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Đăng ký thất bại khi để trống Password",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Đăng ký thất bại khi nhập sai Phone",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "meo",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Đăng ký thất bại khi để trống Phone",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "06",
        "name": "Đăng ký thất bại khi nhập sai định dạng Email",
        "fullname": "hang",
        "email": "hang01",
        "phone": "24012004",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "07",
        "name": "Đăng ký thất bại khi để trống Email",
        "fullname": "hang",
        "email": "",
        "phone": "24012004",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "08",
        "name": "Đăng ký thất bại khi nhập FullName không hợp lệ",
        "fullname": "@!#$",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "expect_success": False
    },
    {
        "id": "09",
        "name": "Đăng ký thất bại khi để trống FullName",
        "fullname": "",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "expect_success": False
    }
]
