TEST_CASES_ADD_CUSTOMER = [
    {
        "id": "TC_KH01",
        "name": "(TH1) Thêm KH thành công",
        "customer_name": "Lê Văn A",
        "phone": "0912345678",
        "email": "a@gmail.com",
        "expect_success": True
    },
    {
        "id": "TC_KH02",
        "name": "(TH8) Để trống Tên KH (B)",
        "customer_name": "",
        "phone": "0912345678",
        "email": "a@gmail.com",
        "expect_success": False
    },
    {
        "id": "TC_KH03",
        "name": "(TH7) Tên KH < 2 ký tự (F)",
        "customer_name": "A",
        "phone": "0912345678",
        "email": "a@gmail.com",
        "expect_success": False
    },
    {
        "id": "TC_KH04",
        "name": "(TH7) Tên KH > 100 ký tự (F)",
        "customer_name": "a"*101,
        "phone": "0912345678",
        "email": "a@gmail.com",
        "expect_success": False
    },
    {
        "id": "TC_KH05",
        "name": "(TH6) Để trống Số điện thoại (B)",
        "customer_name": "Lê Văn B",
        "phone": "",
        "email": "b@gmail.com",
        "expect_success": False
    },
    {
        "id": "TC_KH06",
        "name": "(TH5) Số điện thoại thiếu số (F)",
        "customer_name": "Lê Văn B",
        "phone": "0912",
        "email": "b@gmail.com",
        "expect_success": False
    },
    {
        "id": "TC_KH07",
        "name": "(TH5) Số điện thoại chứa chữ (F)",
        "customer_name": "Lê Văn B",
        "phone": "091234abcd",
        "email": "b@gmail.com",
        "expect_success": False
    },
    {
        "id": "TC_KH08",
        "name": "(TH4) Để trống Email (B)",
        "customer_name": "Lê Văn C",
        "phone": "0912345678",
        "email": "",
        "expect_success": False
    }
]
