TEST_CASES_REGISTER = [
    {
        "id": "01",
        "name": "Đăng ký tài khoản website thành công",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Đăng ký tài khoản thất bại khi để trống “Email”",
        "fullname": "hang",
        "email": "",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Đăng ký tài khoản thất bại khi nhập sai định dạng “Email”",
        "fullname": "hang",
        "email": "hang01",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Đăng ký tài khoản thất bại khi nhập Email trùng/ đã tồn tại trong CSDL",
        "fullname": "hang",
        "email": "nguyen@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Đăng ký tài khoản thất bại khi nhập Email > 20 ký tự",
        "fullname": "hang",
        "email": "nguyenthuhang04122004@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "06",
        "name": "Đăng ký tài khoản thất bại khi nhập Email có chứa ký tự space",
        "fullname": "hang",
        "email": "hang nguyen@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "07",
        "name": "Đăng ký tài khoản thất bại khi bỏ qua trường “Phone”",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "08",
        "name": "Đăng ký tài khoản thất bại khi nhập ký tự chữ vào trường “Phone”",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "meo",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "09",
        "name": "Đăng ký tài khoản thất bại khi nhập Phone trùng/ đã tồn tại trong CSDL",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "12345678",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "10",
        "name": "Đăng ký tài khoản thất bại khi nhập > 11 ký tự số",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "0123456789012",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "11",
        "name": "Đăng ký tài khoản thất bại khi nhập > 20 ký tự vào trường Password",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004240120040",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "12",
        "name": "Đăng ký tài khoản thất bại khi bỏ qua trường Password",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "13",
        "name": "Đăng ký tài khoản thất bại khi nhập “Password” có chứa space",
        "fullname": "hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "0338424  119",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "14",
        "name": "Đăng ký tài khoản thất bại khi nhập space (khoảng trắng) vào trường FullName",
        "fullname": "thu  hang",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "15",
        "name": "Đăng ký tài khoản thất bại khi nhập ký tự số/ ký tự đặc biệt vào trường FullName",
        "fullname": "@!#$",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "16",
        "name": "Đăng ký tài khoản thất bại khi nhập Full Name > 25 ký tự",
        "fullname": "hangthunguyenhangnguyenthu",
        "email": "Hoangtrungmanh24@gmail.com",
        "phone": "24012004",
        "password": "24012004",
        "role": "Teacher",
        "expect_success": False
    },
    {
        "id": "17",
        "name": "Đăng ký tài khoản thất bại khi bỏ trống cả 4 trường",
        "fullname": "",
        "email": "",
        "phone": "",
        "password": "",
        "role": "Teacher",
        "expect_success": False
    }
]
